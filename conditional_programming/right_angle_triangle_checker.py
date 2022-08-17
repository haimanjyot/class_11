side1 = (eval(input('Plese enter the first side --- ')))**2
side2 = (eval(input('Plese enter the second side --- ')))**2
side3 = (eval(input('Plese enter the third side --- ')))**2

if (side1 + side2 == side3) or (side1 + side3 == side2) or (side2 + side3 == side1):
    print('The three sides form a right angle triangle.')
else:
    print('The three sides do not form a right angle triangle.')
