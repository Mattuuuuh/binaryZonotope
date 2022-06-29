import numpy as np
import scipy.linalg as la
import copy 

m=5
n=2**m -1
A=np.eye(m)

# builds complete matrix
for a in np.ndindex((2,)*m):
    if(np.sum(a)>1):
        A=np.vstack((A,a))

A=A.T
print(A)

# loops over (m-1)-dim arrays of decreasing order
def main(x,i=0):
    if i==m-1:
        submatrix(x)
    else:
        if i==0:
            M=n
        else:
            M=x[i-1]
        for k in range(M):
            x[i]=k
            main(x,i+1)

def submatrix(S):
    B=A[np.ix_(range(m),S)]
    c=la.null_space(B.T)
    if (c.shape[1]==1):
        append(np.round(c, 3))

S=[]
def append(c):
    global S
    # is there an easier and faster way to check c is already in S?
    for s in S:
        if np.all(s==c):
            return 1
    S.append(c)
    S.append(-c)
    return 0

main((m-1)*[0])
print(len(S))

# scales u to make it integer, hopefully
def scale(u):
    for i in range(len(u)):
        if(np.abs(u[i])<1 and u[i]!=0):
            u=u/u[i]
    for i in range(1,4): # must increase 4 when m gets big
        if np.all(np.rint(i*u)==i*u):
            return i*u.T
    return u.T

out=np.zeros((len(S),m))

for i in range(len(S)):
    s=S[i]
    out[i,:]=scale(s)

out.tofile("facets"+str(m)+"-full", sep=' ', format='%i')
