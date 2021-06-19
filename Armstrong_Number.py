total=0
num=int(input('enter a number: '))
temp=num
count=len(str(num))
while temp > 0:
    r=temp%10
    total=total+(r**count)
    temp=temp//10
if total == num:
    print(num,'is an armstrong number')
else:
    print(num,'is not an armstrong number')
