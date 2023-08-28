import requests
import time
from bs4 import BeautifulSoup

pages = 0

for i in range(3):
    pages += 1
    linked = f"https://itorrents-igruha.org/newgames/page/{pages}/"
    response = requests.get(linked).text
    soup = BeautifulSoup(response, 'lxml')
    games = soup.find_all('div', class_='article-film')
    for game in games:
        title = game.find('div', class_='article-film-title').text
        link = game.find('a', href=True)
        link_info = link['href']

        response_info = requests.get(link_info).text
        soup_info = BeautifulSoup(response_info, 'lxml')

        info = soup_info.find('div', style='padding-left: 215px;')

        line = [title, link_info, info.text]

        with open('file.txt', 'a', encoding='UTF-8') as file_data:
            file_data.write(str(line)+'\n')
    print(pages)
    time.sleep(2)
