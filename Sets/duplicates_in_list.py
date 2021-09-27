a = [1,1,2,3,4,3,0,0]
res = []
for i in a:
    if i not in res:
        res.append(i)
print(res)
