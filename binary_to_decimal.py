num=input('enter binary number: ')
n=0
for i in range(len(num)):
    if int(num[i])==1:
        n+=2**i
print('number is: ',n)  
