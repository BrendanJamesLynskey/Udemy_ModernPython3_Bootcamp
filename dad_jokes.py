import requests
from random import choice
from pyfiglet import figlet_format 

# Print a large red header
header = figlet_format("Dad joke generator")
print(header)

# Specify Dad Jokes website, with API
dj_url = "https://icanhazdadjoke.com/search"


# Ask for subject of DJs
subject = input("Give me a joke subject:")

# Get the jokes
response = requests.get(
    dj_url,
    headers ={"Accept": "application/json"},
    params  ={"term": subject}
).json()


# Print the DJs
num_jokes = len(response['results'])


if num_jokes == 0:
    print(f"I don't know any jokes about {subject}")
elif num_jokes == 1:
    print(f"\n\tI've got 1 joke about {subject}. Here it is:\n\n")
    print(response['results'][0]['joke'])
else:
    print(f"\n\tI've got {num_jokes} jokes about {subject}. Here's one:\n\n")
    print(choice(response['results'])['joke'])



