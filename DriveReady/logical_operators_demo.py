course = input('enter course: ')
campus = input('enter campus name: ')
year = int(input('enter year: '))
branch = input('enter branch: ')
percentage = int(input('enter percentage: '))
backlogs = int(input('enter number of backlogs: '))
if(course=='btech' and campus=='aec' and year==4 and (branch=='cse' or branch=='it') and percentage>=65 and backlogs==0):
    print('eligible for drive')
else:
    print('not eligible for drive')
