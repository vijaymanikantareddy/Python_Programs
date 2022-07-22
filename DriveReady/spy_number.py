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

num = int(input('enter a number: '))
print(isspy(num))
print(isspynum(num))
