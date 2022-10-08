# WAP to input a sentence from the user and tell how many words there are.

sen = input('Please enter a sentence --- ')

words = sen.split(' ')

print(f'There are/is {len(words)} word(s) in the sentence.')