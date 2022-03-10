import bs4
from bs4 import BeautifulSoup
import requests



def save():
    with open('parse.txt', 'ROI') as file:
        file.write()



def parse():
    URL='https://www.pochta.ru/tracking#14391357849781'
    HEADRS={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    response=requests.get(URL, headers=HEADRS)
    soup=BeautifulSoup(response.content, 'html.parser')
    items=soup.findAll('div', class_='TrackingCardHistory__Layout-zdvopc-0 hydCty')
    comps=[]

    for item in items:
        comps.append({
            'title': item.find('div', class_='TrackingCardHistory__HistoryItem-zdvopc-3 kIXBeA').get_text(strip=True)
        })

        for comp in comps:
            print(comp["title"])

parse()

