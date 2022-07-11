import numpy as np
from numpy.linalg import matrix_rank
import copy 

m=6
A=np.eye(m)

# builds complete matrix
for a in np.ndindex((2,)*m):
    if(np.sum(a)>1):
        A=np.vstack((A,a))

n=len(A)
A=A.T
print(A)

# takes h generated facets
c=np.fromfile("facets"+str(m)+"-gen", sep=' ')
c=np.reshape(c, (int(len(c)/m),m))


# remove opposites
R=[]
for i in range(len(c)):
    print(i, "  /  ", len(c))
    flag=not np.isin(i,R)
    j=i+1
    while(flag):
        print(j, "  /  ", len(c))
        if np.all(c[i,:]==-c[j,:]):
            R.append(j)
            flag=False
        j=j+1
        
c=np.delete(c,R,axis=0)
h=len(c)

# first h hyperplanes
H=np.zeros((h,n))
for i in range(h):
    for j in range(n):
        if c[i,:]@A[:,j]==0:
            H[i,j]=1

print(H)
print(h)

# outputs H_i intersected with H_j
def interesect(i,j):
    return H[i,:]*H[j,:]

# outputs H_i union H_j
def union(i,j):
    return np.maximum(H[i,:],H[j,:])

# adds element k to set h
def add(h,k):
    x=copy.copy(h)
    x[k]=1
    return x

# tests if hyperplane h is included in one of the already defined one
def isincluded(h):
    for i in range(len(H)):
        if(np.all(h <= H[i,:])):
            return True
    return False

# extends h to an hyperplane
def extend(h):
    # takes vectors of h inside matrix B
    indices=np.nonzero(h)[0]
    B=A[:,indices].T

    # goes over unused vector indices, adds vectors to B and checks if rank is m-1
    for i in np.nonzero(np.ones(n)-h)[0]:
        C=np.vstack((B,A[:,i]))
        if matrix_rank(C)==(m-1):
            B=C
            h[i]=1
    return h

# checks if all tuples (H_i, H_j, x) as in Semyour's paper are included in already present hyperplanes. 
# If not, it extends the counterexamples and adds them to H, returns True.
# Returns False if not counterexamples are found.
def hasadded():
    global H
    global h
    flag=False
    # i > j loop over pairs of hyperplanes in H. 
    for i in range(h):
        print(i, " / ", h, "  |  ", len(H)) # ranges to number of facets
        for j in range(i):
            hyp=interesect(i,j)
            # k loops over vector indices not used by h
            for k in np.nonzero(np.ones(n)-union(i,j))[0]:
                x=add(hyp,k)
                if(not isincluded(x)):
                    x=extend(x)
                    H=np.vstack((H,x))
                    flag=True
    return flag
 
# main loop
def main():
    if(hasadded()):
        print("Added new facets. ")
    return 0

main()
print("List had", h, "elements, ie.", 2*h, "facets")
print("Listed ", len(H), " sets, which means ", 2*len(H), " facets.")
