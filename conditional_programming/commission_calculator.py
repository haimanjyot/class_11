sales = eval(input("Please enter the sales done --- "))

commission = 0

if sales <= 0:
    commission = 0
elif sales <= 5000:
    commission = sales * 0.02
elif sales <= 10000:
    commission = (sales - 5000) * 0.03 + 100
elif sales <= 25000:
    commission = (sales - 10000) * 0.05 + 250
else:
    commission = (sales - 25000) * 0.1 + 1000

print(f"The commission earned is {commission}.")
