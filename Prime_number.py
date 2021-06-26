n=int(input('enter a number: '))
flag=0
if n==1:
    print(n,'is neither a composite nor prime number')
else:
    for i in range(2, n):
        if n%i==0:
            flag=1
    if flag==0:
        print(n,'is a prime number')
    else:
        print(n,'is not a prime number')
