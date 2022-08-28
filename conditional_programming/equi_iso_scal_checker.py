side1 = eval(input("Plese enter the first side --- "))
side2 = eval(input("Plese enter the second side --- "))
side3 = eval(input("Plese enter the third side --- "))

if side1 + side2 <= side3:
    print("The three sides do not make a triangle.")
elif side1 == side2 == side3:
    print("The three sides form an equilateral triangle.")
elif (side1 == side2) or (side2 == side3) or (side1 == side3):
    print("The three sides form an isoceles triangle.")
elif (side1 + side2 == side3) or (side1 + side3 == side2) or (side2 + side3 == side1):
    print("The three sides form a right angle triangle.")
else:
    print("The three sides form an scalene triangle")
