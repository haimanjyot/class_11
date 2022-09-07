# WAP to input a number and tell whether it is prime or not.

num = int(input("Enter a number to check if it is prime or not --- "))

if num < 0:
    raise ValueError("Negative numbers can't be prime.")
elif (num == 0) or (num == 1):
    raise ValueError(f"{num} is neither prime nor composite.")

factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

if len(factors) == 2:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is a composite number.")
