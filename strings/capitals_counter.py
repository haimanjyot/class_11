# WAP to input a sentence from the user and tell how many capital letters there are.

sen = input('Please enter a sentence --- ')

count = 0

for i in sen:
    if i.isupper():
        count += 1

print(f'There are {count} capital letters in the sentence.')