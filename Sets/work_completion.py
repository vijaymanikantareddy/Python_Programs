x = int(input('enter x: '))
y = int(input('enter y: '))
z = int(input('enter z: '))
work = (x*y*z)/(x*y + y*z + z*x)
days = round(work,3)
print('work can be completed in',days,'days')
