import requests

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

r = requests.get(f"{baseurl}/{endpoint}")

data = r.json()

pages = data['info']['pages'] 