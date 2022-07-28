
def multiple(a,b):
    s = 0
    while a :
        if(a%2!=0):
            s += b
        a//=2
        b*=2
    return s


def multiplerecur(a,b):
    res=0
    if a==1:
        return b
    if a%2!=0:
        return b+multiplerecur(a//2, b*2)
    else:
        return multiplerecur(a//2, b*2)
    

a,b = map(int, input('enter two numbers: ').split())
print(multiple(a,b))
print(multiplerecur(a,b))





















