# WAP to input a sentence from the user and tell how many words there are.

from curses.ascii import isalpha


sen = input('Please enter a sentence --- ')

words = sen.split(' ')
final = 0
for i in words:
    if i.isalpha():
        final += 1

print(f'There are/is {final} word(s) in the sentence.')