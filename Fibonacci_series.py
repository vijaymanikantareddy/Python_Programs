pt=0
ct=1
n=int(input('enter a number: '))
if n==1:
    print(pt)
elif n==2:
    print(pt)
    print(ct)
else:    
    print(pt)
    print(ct)
    for i in range(3, n+1):
        next= ct+pt
        pt=ct
        ct=next
        print(next)
