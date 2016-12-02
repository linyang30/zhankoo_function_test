import requests
from bs4 import BeautifulSoup


def zhanhui_search(keyword, is_exist):
    url = 'http://exh.zhankoo.com/Exhibition/Partial/_SearchExhibitionFindPage?pageIndex=1&pageSize=1&keyword=%s' % keyword
    web_response = requests.get(url)
    soup = BeautifulSoup(web_response.text, 'lxml')
    if is_exist:
        result = soup.select('a.listpic')[0].get('title')
        assert keyword in result
    else:
        result = soup.select('div.nosearch')
        if result:
            assert True


if __name__ == '__main__':
    zhanhui_search('test', False)