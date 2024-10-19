import os
import requests
from bs4 import BeautifulSoup

DATA_DIRECTORY = 'saved_data/2022BC'
url = 'https://www.nyc.gov/site/buildings/codes/2022-construction-codes.page#bldgs'
base_url = 'https://www.nyc.gov/assets/buildings/codes-pdf/cons_codes_2022/'
response = requests.get(url, timeout=10)

soup = BeautifulSoup(response.content, 'html.parser')

links = []
file_names = []

for a_tag in soup.find_all('a', href=True):
    links.append(a_tag['href'])

for link in links:
    if '2022BC' in link:
        name = link.split('/')[-1]
        if '=' in name:
            name = name.split('=')[1].split('&')[0]
        file_names.append(name)

os.makedirs(DATA_DIRECTORY, exist_ok=True)

for idx, file_name in enumerate(file_names):

    file_url = base_url + file_name
    response = requests.get(file_url, timeout=10)

    file_path = os.path.join(DATA_DIRECTORY, f'{idx}_{file_name}')

    with open(file_path, 'wb') as file:
        file.write(response.content)
