
def gcd(a,b):
    if a<b:
        a,b = b,a
    if b==0:
        return a
    if a%b==0:
        return b
    return gcd(b, a%b)


a,b = map(int, input('enter two numbers: ').split())
print(gcd(a,b))





















