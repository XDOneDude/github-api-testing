import requests
from pprint import pprint
username = "your user"
url = f"https://api.github.com/users/{username}"
user = requests.get(url).json()
pprint(user)