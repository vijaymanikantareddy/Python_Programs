import math as m
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

num = int(input('enter a number: '))
print(issemiprime(num))
