t=2
pro=1
def lcm(a,b):
    i=2
    s=1
    while i<a and i<b:
        if a%i==0 and b%i==0:
            s*=i
            a//=i
            b//=i
        else:
            i+=1
    return s*a*b


def lcmrec(a,b):
    global t
    res =1
    if t>a or t>b:
        return a*b
    if a%t==0 and b%t==0:
        res = t
        a//=t
        b//=t
    else:
        t+=1
    return res*lcmrec(a,b)
    

a, b = map(int, input('enter two numbers: ').split())
print(lcm(a,b))
print(lcmrec(a,b))
