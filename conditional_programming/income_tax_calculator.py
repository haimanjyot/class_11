income = eval(input('Please enter your income --- '))

tax = 0

if income <= 500000:
    tax = 0
elif income <= 800000:
    tax = (income-500000)*0.1
elif income <= 1200000:
    tax = (income - 800000)*0.2 + 30000
elif income <= 2000000:
    tax = (income-1200000)*0.3 + 110000
else:
    tax = (income-2000000)*0.4 + 350000

if income > 500000:
    tax += (income-500000)*0.022

print(f'The tax on your income is {tax}.')
