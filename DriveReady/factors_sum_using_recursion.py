i=1

def factsum(n):
    global i
    res = 0
    if i*i>n:
        return 0
    if n%i==0:
        if i==n//i:
            res += i
        else:
            res += i+(n//i)
    i+=1
    return res+factsum(n)

n = int(input())
print(factsum(n))
