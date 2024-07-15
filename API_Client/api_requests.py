# https://youtu.be/05sP5ST4Bus?list=PLll2u-uqtmZOkjgSczFw1CwnxV3Dw6sEF

import requests
from bs4 import BeautifulSoup

base_url = 'https://gorest.co.in/public/v2/'
end_point = 'users'

r = requests.get(base_url + end_point)
data = r.json()

print(data[0])