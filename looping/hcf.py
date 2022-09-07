# WAP to input two numbers and get their HCF.

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

print(f"The HCF of {num1} and {num2} is {max(factors)}")

# This method only works when both the numbers are positive:

# if num1 > num2:
#     while(num1):
#         num2, num1 = num1, num1 % num2
#     print(f'The HCF is {num2}')
# elif num2 > num1:
#     while(num2):
#         num1, num2 = num2, num2 % num1
#     print(f'The HCF is {num1}')
# else:
#     print(f'The HCF is {num1}')
