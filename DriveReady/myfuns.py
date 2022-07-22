import math as m
def isspy(n):
    su=0
    pro=1
    for digit in str(n):
        su += int(digit)
        pro *= int(digit)
    return su==pro

def isspynum(n):
    s=0
    pro=1
    while n:
        d = n%10
        n//=10
        s+=d
        pro*=d
    return s==pro

def isperfect(n):
    res = 1
    for i in range(2, int(m.sqrt(n))+1):
        if(n%i==0):
            if(i != (n//i):
                res += i + (n//i)
            else:
                res += i
        if res>n:
            return False
    return res==n

def isprime(n):
    for i in range(2, int(m.sqrt(n)+1)):
        if(n%i==0):
            return False
    return True
        
def issemiprime(n):
    for i in range(2, int(m.sqrt(n))+1):
        if(n%i==0):
            if(isprime(i) and isprime(n//i)):
                return True
    return False
