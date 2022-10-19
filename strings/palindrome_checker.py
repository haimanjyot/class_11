# WAP to input a word and tell whether the word is a palindrome or not.

word = input("Please enter a word to check of it is a palindrome --- ")

if word.lower() == word[::-1].lower():
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
