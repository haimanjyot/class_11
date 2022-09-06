# Wap to input a number and display the reverse of the number.

num = int(input('Please enter a number to get its reverse --- '))
num = str(num)

final = ''

for i in range(1, len(num)+1):
    final += num[-1*i]

if final[-1] == '-':
    final = final[:-1]
    final = '-' + final

print(final)