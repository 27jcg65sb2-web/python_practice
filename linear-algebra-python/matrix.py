def mat_vec(A,x):
    n=len(A)
    m=len(x)

    y=[]
    for i in range(n):
        s=0

        for j in range(m):
            s+=A[i][j]*x[j]
            y.append(s)
    return y

A=[[1,2],[3,4]]
x=[5,6]
print(mat_vec(A,x))