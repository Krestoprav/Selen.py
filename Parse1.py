import requests
from bs4 import BeautifulSoup

URL='https://www.pochta.ru/tracking/'
HEADRS={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
response=requests.get(URL, headers=HEADRS)
soup=BeautifulSoup(response.content, 'html.parser')

print(dir(soup))