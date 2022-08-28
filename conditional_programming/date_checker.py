d = int(input("Please enter your date of birth --- "))
m = int(input("Please enter your month of birth --- "))
y = int(input("Please enter your year of birth --- "))

leap_year = False
if y % 100 == 0:
    if y % 4 == 0:
        leap_year = True
elif y % 4 == 0:
    leap_year = True

if leap_year:
    if m in [1, 3, 5, 7, 8, 10, 12]:
        if (d > 31) or (d < 1):
            print("Something is wrong!!!")
        else:
            print("The date seems fine.")
    elif m in [4, 6, 9, 11]:
        if (d > 30) or (d < 1):
            print("Something is wrong!!!")
        else:
            print("The date seems fine.")
    elif m == 2:
        if (d > 29) or (d < 1):
            print("Something is wrong!!!")
        else:
            print("The date seems fine.")
    else:
        print("Something is wrong!!!")
else:
    if m in [1, 3, 5, 7, 8, 10, 12]:
        if (d > 31) or (d < 1):
            print("Something is wrong!!!")
        else:
            print("The date seems fine.")
    elif m in [4, 6, 9, 11]:
        if (d > 30) or (d < 1):
            print("Something is wrong!!!")
        else:
            print("The date seems fine.")
    elif m == 2:
        if (d > 28) or (d < 1):
            print("Something is wrong!!!")
        else:
            print("The date seems fine.")
    else:
        print("Something is wrong!!!")
