num = int(input("Please enter a number to check if it is odd or even --- "))

if num == 0:
    print(f"{num} is neither odd nor even.")
elif num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
