import numpy as np
import scipy.linalg as la
import copy 

m=6
n=2**m -1
#c=[[1],[-1]] # for first iteration, m=2
c=np.fromfile("facets"+str(m-1)+"-full", sep=' ')
c=np.reshape(c, (int(len(c)/(m-1)),(m-1)))

print(np.shape(c))

x=np.zeros(m)
x[m-1]=1
C=np.array([x]) 

# concatenates an element of c with the opposite of an element of its binary image
def main():
    for n in c:
        I=image(n)
        for i in I:
            N=np.concatenate(([-i],n))
            append(N)
            append(-N)
        # adds nothing ):
        """
        if np.sum(np.abs(n))!=1:
            for i in range(m-1):
                N=np.concatenate(([n[i]],n))
                if np.all(n==[2,-1,-1,-1]):
                    print(N)
                append(N)
        """

# computes binary image of n
def image(n):
    S=set()
    for v in np.ndindex((2,)*(m-1)):
        S.add(np.dot(v,n))
    return S

# checks if N is in array C and appends it if not
def append(N):
    global C
    # is there an easier and faster way to check N is already in C?
    for s in C:
        if np.all(s==N):
            return 1
    C=np.vstack((C,N))
    return 0

# goes through elements of C and swaps the first coordinate with the m-1 other; appends that to C
def addperm():
    global C
    for i in range(m-1):
        print(i, " / ", m-1)
        for c in C:
            if c[0]!=c[i+1]:
                d=copy.copy(c)
                d[0]=c[i+1]
                d[i+1]=c[0]
                append(d)
                append(-d)

main()
C=np.array(C)
print(len(C))
addperm()
#print(C)
print(len(C), " facets in dimension ", m, " generated from dimension ", m-1)
C.tofile("facets"+str(m)+"-gen", sep=' ', format='%i')
