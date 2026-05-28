def can_multiply(A,B):
    return len(A[0]) == len(B)
def matrix(A):
    if len(A) == 0:
        return False
    r=len(A[0])
    for row in A:
        if len(row) != r:
            return False
        
    return True
def shape(A):
    if not matrix(A):
        raise ValueError("not matrix")
    return (len(A),len(A[0]))
def zeros(n,m):
    y=[]
    for i in range(n):
        x=[]
        for l in range(m):
            x.append(0)
        y.append(x)
    return y



def mat_mul(A,B):
    if not can_multiply:
        raise ValueError("matrix size mismatch")
    if not matrix(A):
        raise ValueError("A is not matrix")
    if not matrix(B):
        raise ValueError("B is not matrix")
    if len(A[0]) != len(B):
        raise ValueError("matrix size missmatch")
    l=len(A)
    d=len(B)
    c=len(B[0])
    y=[]
    for i in range(0,l):
        x=[]
        for m in range(0,d):
            x0=0
            for n in range(0,c):
                x0+=A[i][n]*B[n][m]
            x.append(x0)
        y.append(x)
    return y

A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
print(mat_mul(A,B))

