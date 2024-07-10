import requests
from bs4 import BeautifulSoup
import pandas as pd

#https://www.youtube.com/watch?v=tb8gHvYlCFs&t=1127s
#https://www.youtube.com/watch?v=-oPuGc05Lxs

documentation_end_point = 'documentation'

base_url = 'https://rickandmortyapi.com/api/'
end_point= 'character'

def main_request(base_url,end_point,x):
    r = requests.get(base_url+end_point+f'?page={x}')
    data = r.json() #return json/dict
    return data

def get_pages(response):
    return response['info']['pages']


def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {
            'id': item['id'],
            'name': item['name'],
            'num_of_episode': len(item['episode']),
        }
        charlist.append(char)
    return charlist

mainlist = []
data = main_request(base_url, end_point,1)
for x in range(1,get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(base_url,end_point, x)))

# print(len(mainlist))
# print(get_pages(data))
# print(parse_json(data))

dataframe = pd.DataFrame(mainlist)
# print(dataframe.head(), dataframe.tail())#<====Print out to console


dataframe.to_csv('charlist.csv', index=False)