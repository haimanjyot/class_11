# WAP to input an email address and display the username and domain name separatley.

email = input('Please enter your email --- ')
separated = email.split('@')

print(f'Username - {separated[0]}\nDomain Name - {separated[1]}')