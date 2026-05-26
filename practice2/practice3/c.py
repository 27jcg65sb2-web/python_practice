n0=int(input("初期値"))
l=int(input("一年で入れられる金額"))
n=int(input("年数"))
def p(n0,l,n):
    y=0
    for i in range(0,n):
        y=y*(1.05)+l
    return y
print(p(n0,l,n))
