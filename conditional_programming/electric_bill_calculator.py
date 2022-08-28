units = eval(input("Please enter the number of units consumed --- "))

while units < 0:
    print("The units can't be less than zero.")
    units = eval(input("Please enter the number of units consumed --- "))


def generator(x):
    if x <= 100:
        return x * 0.8
    elif x <= 250:
        return 80 + (x - 100)
    elif x <= 400:
        return 230 + ((x - 250) * 1.2)
    else:
        return 410 + ((x - 400) * 1.5)


print(f"The bill generated is {generator(units)}.")
