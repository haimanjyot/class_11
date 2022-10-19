# WAP to input a sentence and capitalize the first letter of each word in it.

sen = input('Please enter a sentence --- ')
seperated = sen.split()
final = ''

for i in seperated:
    final += f'{i.capitalize()} '

final = final[:-1]

print(final)

'''
Method using .capwords():
sen = sen.capwords()
'''