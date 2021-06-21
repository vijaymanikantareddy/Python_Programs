#GCD of two numbers
num1=int(input('enter number 1: '))
num2=int(input('enter number : '))
while True:
    if num1 >= num2 :
        num1=num1-num2
    else:
        num1, num2= num2, num1
    if num1==0 :
        break
print(num2)   
