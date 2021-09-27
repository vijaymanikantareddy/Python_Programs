flag=0
s=input('enter a string: ')

#using slicing
a = s[::-1]
if s==a:
    print('string is palindrome')
else:
    print('string is not palindrome')
    
#using loop
for i in range(len(s)):
    if s[i]==s[len(s)-i-1]:
        flag+=1
    else:
        break
if flag==len(s):
    print('string is palindrome')
else:
    print('string is not palindrome')
