import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    r.encoding = 'win1251'
    return r.text


def csv_read(data):
    with open("data.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['head'], data['link']))

def get_link(html):
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find('div', id='section-content').find_all('a', class_="entry-header")
    for i in head:
        link = 'https://3dnews.ru' + i.get('href')
        heads= i.find('h1').string
        data = {'head': heads,
                 'link': link}
        csv_read(data)



def main():
    data = get_link(get_html('https://3dnews.ru/news'))
    print('Every thing is Fine! Please look at file data.csv, Thank You so much!')

if __name__ == '__main__':
    main()

