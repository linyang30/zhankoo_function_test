import requests
from bs4 import BeautifulSoup


def zhanzhuang_search(keyword, is_exist):
    url = 'http://exh.zhankoo.com/Decorate/Partial/_DecorateSearchPage?pageIndex=1&pageSize=1&keyword=%s' % keyword
    web_response = requests.get(url)
    soup = BeautifulSoup(web_response.text, 'lxml')
    if is_exist:
        result = soup.select('span.zd_one a')[0].get('title')
        assert keyword in result
    else:
        result = soup.select('div.nosearch')
        if result:
            assert True

if __name__ == '__main__':
    zhanzhuang_search('风尚', True)