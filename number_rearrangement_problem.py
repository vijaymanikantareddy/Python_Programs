l = [1,3,4,6,8,2,5,7,9]
sa = set(l)
a = list(sa)
l.sort()
b = l
length = len(l)//2
outl = []
final = []
if a != l: #if duplicates are found it stops executing
    print('Invalid Input')
else:
    for i in range(length+1):
        outl.append(l[-i-1])
        outl.append(l[i])
    for i in outl:
        if i not in final:
            final.append(i)
    print(final)

    
'''
OUTPUT:
[9, 1, 8, 2, 7, 3, 6, 4, 5]
prints alternative numbers like 1st largest and 1st smallest and then 2nd largest and 2nd smallest and soon.....
'''
