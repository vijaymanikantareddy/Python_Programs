n=int(input('enter the number: '))
#case-1
for i in range(1,n+1):
	print('\n')
	for j in range(1,i+1):
		print('*', end=' ')
		
#case-2
for i in range(0, n):
    print((i+1)*"* ")

#output
#enter the number: 4
# *
# * *
# * * *
# * * * *
