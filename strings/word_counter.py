# WAP to input a sentence from the user and tell how many words there are.

sen = input('Please enter a sentence --- ')

words = sen.split()
final = len(words)

print(f'There are/is {final} word(s) in the sentence.')