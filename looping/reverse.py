# Wap to input a number and display the reverse of the number.

num = int(input('Please enter a number to get its reverse --- '))
# num = str(num)

# final = ''

# for i in range(1, len(num)+1):
#     final += num[-1*i]

# if final[-1] == '-':
#     final = final[:-1]
#     final = '-' + final

# print(final)

final = 0

if num < 0:
    num = num*-1

    for i in range(len(str(num))):
        final += (num%10)*(10**(len(str(num))-1))
        num = num//10

    final = final*-1
else:
    for i in range(len(str(num))):
        final += (num%10)*(10**(len(str(num))-1))
        num = num//10

print(final)