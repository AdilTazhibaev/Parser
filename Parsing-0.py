import requests
from bs4 import BeautifulSoup
import csv

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }



base_url = 'https://www.zakon.kz/2019/11/07/'

urls = ''

response = requests.get(base_url)
html = response.text
multi_class = 'cat_news_item'.split(' ')

soup = BeautifulSoup(html, 'html.parser')

news = soup.find_all('div',{'class':'cat_news_item'})

all_news = []
for new_con in news:
    if new_con.attrs['class'] == multi_class:
        data = new_con.find('span',{'class' : 'tahoma font12 date n3'})
        name = new_con.find('a',{'class' : 'tahoma font12'})
        urls = new_con.find('a')
        coment = new_con.find('span',{'class' : 'comm_num'})
        all_news.append([name, data, urls, coment])

        

names = ['Время' , 'Заголовок' , 'Комментарии']

with open('data.csv','w' , newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(names)

    for new_con in all_news:
        writer.writerow(new_con)
        