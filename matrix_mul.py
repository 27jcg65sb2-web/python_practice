def mat_mul(A,B):
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

