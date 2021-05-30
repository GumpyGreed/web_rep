import sys
import requests

url = f'https://kidkodschool.github.io/welcome.html'

response = requests.get(url)

with open("./python_is_cool.html", 'wb') as f:
    f.write(response.content)

from bs4 import BeautifulSoup

query = sys.argv[1] if len(sys.argv) > 1 else input('Введите тип вашего аватара: ')

url = f'https://www.kiddle.co/s.php?q={query}'

page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')



for raw_img in soup.find_all('img'):
    link = raw_img.get('src')
    if link and link.startswith('https'):
        response = requests.get(link)
        with open("./todey_avatar.jpg", 'wb') as f:
            f.write(response.content)
        print('Аватар найден - today_avatar.jpg')
        break
else:
    print('Аватар не найден - today_avatar.jpg')