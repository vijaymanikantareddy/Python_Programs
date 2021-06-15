pt=0
ct=1
n=int(input('enter a number: '))
for i in range(1, n+1):
    next= ct+pt
    pt=ct
    ct=next
    print(next)
