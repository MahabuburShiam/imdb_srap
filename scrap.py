import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
}

url = 'https://www.imdb.com/chart/top/'
try:
    source = requests.get(url, headers=headers)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    #print(soup.prettify())  # optional: use prettify() to make it more readable
except Exception as e:
    print(e)