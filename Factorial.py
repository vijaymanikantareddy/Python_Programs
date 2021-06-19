import math
n=int(input('Enter a number: '))
fact=1
for i in range(1, n+1):
    fact*=i
digits=str(fact)
print('\nNumber of digits in',n,'factorial is',len(digits))    
print('\nFactorial of',n,'without using factorial function is\n',fact)
print('\nFactorial of',n,'with using factorial function is\n',math.factorial(n))
