n=int(input('enter a number : '))
count=0
if n==1:
    print(n,'is neither prime nor composite number')
elif n==0:
    print('enter a valid number')
else:    
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if count==0:
        print(n,'is a prime number')
    else:
        print(n,'is a composite number')
