# WAP to input a word and display it in such a way that the charachters at odd indexes are uppercase and the ones at even indexes are lowercase.

word = input('Please enter a word --- ')
final = ''

for i in range(len(word)):
    if i%2 != 0:
        final += word[i].upper()
    else:
        final += word[i].lower()

print(final)