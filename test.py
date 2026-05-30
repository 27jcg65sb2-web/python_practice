def zeros(n,m):
    r=[]
    for i in range(n):
        r1=[]
        for l in range(m):
            r1.append(0)
        r.append(r1)
    return r

def transpose(A):
    l=len(A)
    r=len(A[0])
    B=zeros(r,l)
    for i in range(l):
        for m in range(r):
            B[m][i]=A[i][m]
    return B
def is_matrix(A):
    a=len(A)
    if a == 0:
        raise ValueError("Not matrix")
    else:
        return True
def can(A,B):
    l=len(A[0])
    r=len(B)
    if not l == r:
        return False
    else:
        return True
    
def mat_mul(A,B):
    if not is_matrix(A) == True:
        raise ValueError("A is not matrix")
    if not is_matrix(B) == True:
        raise ValueError("B is not matrix")
    if not can(A,B) == True:
        raise ValueError("No")
    
    l=len(A)
    r=len(B)
    n=len(B[0])
    result=zeros(l,n)

    for i in range(l):
        for m in range(n):
            for t in range(r):
                result[i][m]+=A[i][t]*B[t][m]
    return result

def identity(n):


    result=zeros(n,n)
    for i in range(n):
        result[i][i]=1

    return result

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [1, 0],
    [0, 1],
    [1, 1]
]
left = transpose(mat_mul(A, B))

right = mat_mul(
    transpose(B),
    transpose(A)
)

print(left)
print(right)



    

    


