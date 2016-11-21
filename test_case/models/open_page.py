import requests
from bs4 import BeautifulSoup

def open(url):
    web_response = requests.get(url)
    soup = BeautifulSoup(web_response.text, 'lxml')
    title = soup.select('head > title')[0].get_text()
    assert '展酷网' in title