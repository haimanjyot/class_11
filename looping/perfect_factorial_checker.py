# WAP to input a number and tell whether it is a perfect factorial or not. A perfect factorial is one in which the sum of factorials of all digitts is equal to the number.

num = int(
    input("Please enter a number to check if it is a perfect factorial or not --- ")
)

if num < 0:
    raise ValueError("Negative numbers do not have a factorial.")

digits = []
a = num

for i in range(len(str(num))):
    digits.append(a % 10)
    a = a // 10

final = 0
temp = 1

for v in digits:
    if v == 0:
        final += 1
    else:
        for i in range(1, v + 1):
            temp *= i
        final += temp
        temp = 1

if final == num:
    print(f"{num} is a perfect factorial.")
else:
    print(f"{num} is not a perfect factorial.")
