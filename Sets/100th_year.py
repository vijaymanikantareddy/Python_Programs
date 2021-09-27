from datetime import date
today_date = date.today()
name = input('enter name: ')
age = int(input('enter age: '))
y = today_date.year-age
print('your 100th year is',y+100)
