def reverse(x):
    rev = 0
    while(x != 0):
        rev = rev*10 + x%10
        x = x//10
    return rev

def make_palindrome(y):
    add = 0
    sub = 0
    while(n+add != reverse(n+add)):
        add += 1
    while(n-sub != reverse(n-sub)):
        sub += 1
    print(f'To make {n} a palindrome, add {add} or subtract {sub}.')

n = int(input('Enter a number: '))

if n == reverse(n):
    print(f'{n} is already a palindrome.')
else:
    make_palindrome(n)