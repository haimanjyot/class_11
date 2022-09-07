# WAP to input a number and tell whether the number is a palindrome or not.

num = int(input('Please enter a nnumber to check of it is a palindrome --- '))

num = str(num)

if num == num[::-1]:
    print(f'{num} is a palindrome.')
else:
    print(f'{num} is not a palindrome.')