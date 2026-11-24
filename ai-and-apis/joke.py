import requests

URL = 'https://icanhazdadjoke.com'

r = requests.get(URL, headers={"Accept":"application/json"}, timeout=10)
r.raise_for_status()
print(r.json())
joke = r.json()["joke"]
print(joke)