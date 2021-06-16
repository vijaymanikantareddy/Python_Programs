pt=0
ct=1
n=int(input('enter a number: '))
print(pt, end=' ')
print(ct, end=' ')
for i in range(3, n+1):
    next= ct+pt
    pt=ct
    ct=next
    print(next, end=' ')
