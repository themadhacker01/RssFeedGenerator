import requests
from bs4 import BeautifulSoup

WEB_URL = 'https://a16z.com/news-content/'

page = requests.get(WEB_URL)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup)

title = soup.title.text
div_list = soup.find('div', class_ = 'heading')

print(div_list)