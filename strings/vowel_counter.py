# WAP to input a sentence from the user and tell how many vowels there are.

sen = input('Please enter a sentence --- ')
vowels = ('a', 'e', 'i', 'o', 'u')

count = 0

for i in sen:
    if i.lower() in vowels:
        count += 1

print(f'There are {count} vowels in the sentence.')