import requests
from bs4 import BeautifulSoup

def open(url):
    web_response = requests.get(url)
    soup = BeautifulSoup(web_response.text, 'lxml')
    title = soup.select('head > title')[0].get_text()
    assert '展酷' in title

def open_links(links, error_links):
    if links:
        try:
            for link in links:
                open(link)
        except Exception:
            error_links.append(link)
        if len(error_links) != 0:
            print(error_links)
            assert False