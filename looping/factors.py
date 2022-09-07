# WAP to input a number and get its factors.

num = int(input('Please enter a number to get its factors --- '))

factors = []

if num < 0:
    num *= -1
    for i in range(1, num+1):
        if num%i == 0:
            factors.append(i)
            factors.append(i*-1)
else:
    for i in range(1, num+1):
        if num%i == 0:
            factors.append(i)

print(f'The factors of {num} are:')
for i in range(len(factors)):
    print(f'{i+1}) {factors[i]}')