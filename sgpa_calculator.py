'''enter marks in order that the result pdf contains
for A++ grade enter o
for A grade enter a
for B grade enter b
for C grade enter c
for D grade enter d
for E grade enter e
for F grade enter f

*** Ignore PPSC Lab grade***
'''

roll_number = input('enter your roll number: ')
m = 0
for i in range(7):
    g = input('enter grade: ')
    if g == 'o':
        n = 10
    elif g == 'a':
        n = 9
    elif g == 'b':
        n = 8 
    elif g == 'c':
        n = 7
    elif g == 'd':
        n = 6
    elif g == 'e':
        n = 5
    else:
        n = 0
    if i==0 or i==1 or i==3 or i==4 or i==6:
        m = m + n*3
    elif i==2 or i==5:
        m = m + n*1.5
        
credits = m/19.5
print('GPA is', credits)
print((m+13.5)/19.5) #if ppsc lab is A
print((m+15)/19.5)  #if ppsc lab is A+
