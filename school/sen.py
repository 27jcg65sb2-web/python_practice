def u(x):
    ##xはn字正方行列
    d=len(x)
    for i in range(d):
       
        for l in range(i+1,d):
             c = x[l][i]/x[i][i]
             for n in range(i,d):
                x[l][n]=x[l][n]-c*x[i][n]
    return x
##v(x,b)はbにガウス法のない
def v(x,b):
    d=len(x)
    y=[]
    a=[]
    y.append(b[d-1]/x[d-1][d-1])
    for i in range(1,d):
        xs=0
        for l in range(i):
            xs+=x[d-i-1][d-l-1]*b[l]
        y.append(xs/x[d-i-1][d-i-1])
    return y
    





            