num=int(input('enter a number: '))
rev=0
while True:
    r=num%10
    rev=rev*10+r
    num=num//10
    if num==0:
        break
print(rev)


#2nd method
print(str(num)[::-1])
