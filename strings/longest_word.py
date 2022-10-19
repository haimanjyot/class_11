# WAP to display the longest word in a sentence.

sen = input('Please enter a sentence --- ')
seperated = sen.split()

lens = [len(i) for i in seperated]
a = lens.index(max(lens))

print(f'The longest word is - "{seperated[a]}"')