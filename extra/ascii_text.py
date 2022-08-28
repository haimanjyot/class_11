from pyfiglet import figlet_format as format
from termcolor import colored

valid_colors = ('grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

msg = input('Please enter the message --- ')
color = (input('\nPlease enter the desired color (Grey, Red, Green, Yellow, Blue, Magenta, Cyan, White) --- ')).lower()

if color not in valid_colors:
    color = 'green'
    print('Since you did not enter a valid color, the text would be printed in green.\n')

print('\n' + colored(format(msg), color = color))