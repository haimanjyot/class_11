import requests
from termcolor import colored
from pyfiglet import figlet_format

print(colored(text=figlet_format("Dad Jokes 999"), color="magenta"))

query = input("Please enter a search term --- ")

res = requests.get(
    url="https://icanhazdadjoke.com/search",
    params={"term": query},
    headers={"accept": "application/json"},
)

jokes = res.json()["results"]
total = res.json()["total_jokes"]

if total == 0:
    print(f'I could not find a joke based on "{query}", so here is a random joke:\n')
    print(
        requests.get(
            url="https://icanhazdadjoke.com",
            headers={"accept": "text/plain"},
        ).text
    )
else:
    print(f'I could find {total} jokes based on "{query}":\n')
    for i in range(total):
        print(f'{i+1}. {res.json()["results"][i]["joke"]}')
