s=input('enter a binary number: ')
rev=s[::-1]
n=0
for i in range(len(rev)):
    if rev[i]=='1':
        n+=2**i
print('binary number is decimal number is :', n) 
