import math as m
def  sqr(n):
    return n*n

def ishappys(n):
    if len(str(n))==1:
        return n==1 or n==7
    s=0
    for i in str(n):
        s += sqr(int(i))
    return ishappys(s)

def ishappynum(n):
    if n//10==0:
        return n==1 or n==7
    s=0
    while n:
        d = n%10
        s += sqr(d)
        n//=10
    return ishappynum(s)
        


n = int(input('enter a number: '))
print(ishappys(n))
print(ishappynum(n))

