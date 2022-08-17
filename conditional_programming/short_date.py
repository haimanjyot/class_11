d = int(input('Please enter your date of birth --- '))
m = int(input('Please enter your month of birth --- '))
y = int(input('Please enter your year of birth --- '))

leap_year = False
if y%100 == 0:
    if y%4==0:
        leap_year=True
elif y%4 == 0:
    leap_year=True

alright=False

if leap_year:
    if m in [1,3,5,7,8,10,12]:
        if (d > 31) or (d<1):
            print('Something is wrong!!!')
            alright=False
        else:
            alright=True
    elif m in [4,6,9,11]:
        if (d > 30) or (d<1):
            print('Something is wrong!!!')
            alright=False
        else:
            alright=True
    elif m == 2:
        if (d > 29) or (d<1):
            print('Something is wrong!!!')
            alright=False
        else:
            alright=True
    else:
        print('Something is wrong!!!')
        alright=False
else:
    if m in [1,3,5,7,8,10,12]:
        if (d > 31) or (d<1):
            print('Something is wrong!!!')
            alright=False
        else:
            alright=True
    elif m in [4,6,9,11]:
        if (d > 30) or (d<1):
            print('Something is wrong!!!')
            alright=False
        else:
            alright=True
    elif m == 2:
        if (d > 28) or (d<1):
            print('Something is wrong!!!')
            alright=False
        else:
            alright=True
    else:
        print('Something is wrong!!!')
        alright=False

months = {
    1:'January'
    2:'Feburary'
    3:'March'
    4:'April'
    5:'May'
    6:'June'
    7:'July'
    8:'August'
    9:'September'
    10:'October'
    11:'November'
    12:'December'
    }

if alright == True:
    print(f'You were born on {d}th {months[m]}, {y}')
