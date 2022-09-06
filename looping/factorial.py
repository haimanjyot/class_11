# WAP to input a number and find the factorial of that number.

num = int(input('Please enter a number to find its factorial --- '))

if num < 0:
    raise ValueError('Negative numbers do not have a factorial.')

# from math import factorial
# print(f'The factorial of {num} is {factorial(num)}.')

final = 1

if num == 0:
    print('The factorial of 0 is 1.')
else:
    for i in range(1,num+1):
        final *= i
    print(f'The factorial of {num} is {final}.')