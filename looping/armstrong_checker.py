# WAP to input a number and tell whether it is armstrong or not. An armstrong number is when the sum of the cubes of the digits is equal to the number itself.

num = int(input('Please enter a number to check if it is an armstrong number or not --- '))

if num < 0:
    print(f'{num} is negative and therefore is not an Armstrong number.')

digits = []
final = 0 
a = num

for i in range(len(str(num))):
    digits.append(a%10)
    a = a//10

for i in digits:
    final += i**3

if final == num:
    print(f'{num} is an armstrong number.')
else:
    print(f'{num} is not an armstrong number.')