s=input('enter a string: ')
l=flag=0
r=len(s)-1
while l<r:
    if s[l] != s[r]:
        flag=0
        break
    else:
        flag+=1
        l+=1
        r-=1
if flag==0:
    print('String is not Palindrome')
else:
    print('String is Palindrome')
