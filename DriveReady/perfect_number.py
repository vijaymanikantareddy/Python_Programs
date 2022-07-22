import math as m
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

t = int(input('enter testcases: '))
for _ in range(t):
    n = int(input('enter a number: '))
    if isperfect(n):
        print(n,'is a perfect number')
    else:
        print(n,'is NOT a perfect number')
