import requests
from termcolor import colored
from pyfiglet import figlet_format

print(colored(text=figlet_format('Dad Jokes 999'), color='magenta'))

query = input('Please enter a search term --- ')

res = requests.get(url='https://icanhazdadjoke.com/search', params={'term' : query}, headers={'accept' : 'text/plain'})

if res.text:
    print(f'\nHere are all the dad jokes I could find based on "{query}":')
    print(res.text)
else:
    print(f'\nI could not find a joke based on "{query}" so here is a random joke:')
    print((requests.get(url='https://icanhazdadjoke.com', headers={'accept' : 'text/plain'})).text)