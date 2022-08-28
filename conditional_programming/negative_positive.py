num = eval(input("Please enter a number to check if it is positive or negative --- "))

if num == 0:
    print(f"{num} is neither positive nor negative.")
elif num > 0:
    print(f"{num} is positive.")
else:
    print(f"{num} is negative.")
