def fun(num):
    if num>=1:
        fun(num//2)
        print(num%2, end='')

n=int(input('enter a number: '))
print('number in binary form is: ',end='')
if n == 0:
    print(0)
else:
    fun(n)
