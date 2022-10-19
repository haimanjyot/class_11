# WAP to input a sentence and display it in such a way that all the even words are in lower case and all the odd words are in uppercase.

sen = input('Please enter a sentence --- ')
seperated = sen.split()
final = ''

for i in range(len(seperated)):
    if i%2 != 0: # Even words since index starts from zero.
        final += f'{seperated[i].lower()} '
    else:
        final += f'{seperated[i].upper()} '

final = final[:-1]

print(final)