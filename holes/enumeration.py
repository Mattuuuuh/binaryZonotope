import numpy as np
import copy
import gurobipy as gp
from gurobipy import GRB

m=9

# builds matrix with at most 3 ones vectors
A=np.eye(m)
for a in np.ndindex((2,)*m):
    if(np.sum(a)<=3 and np.sum(a)>1):
        A=np.vstack((A,a))
n=len(A)
A=A.T
print(A)

# computes the first entry of A@1 to get the maximal possible value of b
maxvalues=int((A@np.ones(n))[0])

# computes total number of b's to visit (to show progress)
t=1
s=1
for k in range(1,m+1):
    t=t*k
for k in range(maxvalues+1, m+maxvalues+1):
    s=s*k
totb=int(s/t)

# loops over m-dim arrays of non-increasing order
numberb=0
def main(x,i):
    if i==m:
        global numberb
        numberb=numberb+1
        print(numberb, "  /  ", totb, "( ", numberb/totb, " )")
        solve(x)
    else:
        if i==0:
            M=maxvalues+1
        else:
            M=x[i-1]+1
        for k in range(M):
            x[i]=k
            main(x,i+1)

i=0
S=[]
T=[]
M=gp.Model()
M.setParam('OutputFlag', 0)
x=M.addMVar(shape=n, vtype="S", lb=0, ub=1)
constr=M.addConstr(A@x == np.zeros(m))

#solves Ax=b for 0<=x<=1, and if it's feasible, solves Ax=b for x in {0,1}

def solve(b):
    constr.RHS=b
    x.vtype="S"
    M.optimize()
    if(M.status == 2): # LP is solved
        x.vtype="B" 
        M.optimize()
        if(M.status != 2): # IP is not solved
            S.append(copy.copy(b))
    elif(M.status != 3): # LP is not unfeasible somehow?
        T.append(copy.copy(b))

main(m*[0],0)

print("There are ", len(S), " vertices that are fractionally but not integrally representable")
print(S)
print("There are ", len(T), " vertices with no IP solution but with LP not proven to be infeasible")
print(T)
