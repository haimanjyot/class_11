"""
WAP to input the complete name and do the following (ex. - Mohan Lal Avasthi):
a) Display the name in initials (M.L.A.)
b) Display the short name (M.L. Avasthi)
c) Display the name in Bibliography format (Avasthi, M.L.)
"""

sen = input('Please enter your full name --- ')

words = sen.split()

initials = ''
for i in words:
    initials += f'{i[0].upper()}.'

short_name = f'{initials[:-2]} {words[-1].capitalize()}'

bib_format = f'{words[-1].capitalize()}, {initials[:-2]}'

print(f'The initals are {initials}')
print(f'The short name is {short_name}')
print(f'The name in bibliography format is {bib_format}')