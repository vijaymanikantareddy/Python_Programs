j = 2

def primerecur(n, i=2):
    if i*i>n:
        return True
    if n%i!=0:
        return primerecur(n, i+1)
    else:
        return False

def isprimerec(n):
    global j
    if j*j>n:
        return True
    if n%j==0:
        return False
    else:
        j+=1
        return isprimerec(n)


n = int(input('enter a number: '))
print(primerecur(n))
print(isprimerec(n))
