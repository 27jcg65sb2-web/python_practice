from matrix_mul import matrix,zeros

def transpose(A):
    if not matrix(A):
        raise ValueError("not matrix")
    n=len(A)
    m=len(A[0])
    y=zeros(m,n)
    for i in range(n):
        for l in range(m):
            y[l][i]=A[i][l]
    return y
A=[[1,2,3],[4,5,6]]
print(transpose(A))