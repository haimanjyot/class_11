# WAP to input a number and check whether it is a SUNNY number or not. A SUNNY number is one whose square root +1 returns a whole number.

from math import sqrt

num = eval(input('Please enter a number to check if it is a SUNNY number or not --- '))

if num < -1:
    raise ValueError('SUNNY numbers are not possible for numbers less than "-1".')

a = sqrt(num+1) # sqrt() returns a float.

if a.is_integer():
    print(f'{num} is a SUNNY number.')
else:
    print(f'{num} is not a SUNNY number.')