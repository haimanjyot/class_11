# WAP to input two numbers and get their LCM.

num1 = int(input("Please enter the first number --- "))
num2 = int(input("Please enter the first number --- "))

factors1 = []
factors2 = []

if num1 < 0:
    num1 *= -1
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            factors1.append(i)
            factors1.append(i * -1)
else:
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            factors1.append(i)

if num2 < 0:
    num2 *= -1
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            factors2.append(i)
            factors2.append(i * -1)
else:
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            factors2.append(i)

factors = [a for a in factors1 if a in factors2]

print(f'The LCM of {num1} and {num2} is {(num1*num2)/max(factors)}')