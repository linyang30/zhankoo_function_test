import unittest
from bs4 import BeautifulSoup
import requests
from test_case.models.open_page import open, open_links
import json
import re

class SearchResult(unittest.TestCase):

    zhanhui_search_result_url = 'http://exh.zhankoo.com/Exhibition/Partial/_SearchExhibitionFindPage?pageIndex=1&pageSize=1000'
    zhanzhuang_search_result_url = 'http://exh.zhankoo.com/Decorate/Partial/_DecorateSearchPage?pageIndex=1&pageSize=1000'
    xiaoguotu_search_result_url = 'http://exh.zhankoo.com/Decorate/DecorateCase/DecorateCaseSearchJson'
    zhanguan_data_url = 'http://exh.zhankoo.com/Pavilion/Partial/_PavilionIndexPage'
    txzhanshang_data_url = 'http://txzhanshang.zhankoo.com/Partial/_IndexListArchiles'
    zhanhui_links = []
    zhanzhuang_links = []
    zhanhui_links_error = []
    zhanzhuang_links_error = []
    xiaoguotu_ids = []
    xiaoguotu_links_error = []
    zhanguan_links_error = []


    def test_zhanhui_serach_result(self):
        '''获取所有展会数据，并依次打开所有展会详情页'''
        web_response = requests.get(self.zhanhui_search_result_url)
        soup = BeautifulSoup(web_response.text, 'lxml')
        targets = soup.select('div.searchlist > ul > li > a')
        for target in targets:
            self.zhanhui_links.append('http:' + target.get('href'))
        assert len(self.zhanhui_links) > 600
        open_links(self.zhanhui_links, self.zhanhui_links_error)


    def test_zhanzhuang_search_result(self):
        '''获取所有展装数据，并依次打开所有展装详情页'''
        web_response = requests.get(self.zhanzhuang_search_result_url)
        soup = BeautifulSoup(web_response.text, 'lxml')
        targets = soup.select('span.zd_one > h3 > a')
        for target in targets:
            self.zhanzhuang_links.append('http:' + target.get('href'))
        assert len(self.zhanzhuang_links) > 600
        open_links(self.zhanzhuang_links, self.zhanzhuang_links_error)


    def test_xiaoguotu_search_result(self):
        '''获取所有效果图数据，并打开前20个效果图详情页'''
        data = {
            'pageIndex': 1
        }
        web_response = requests.post(self.xiaoguotu_search_result_url, data=data)
        result_json = json.loads(web_response.text)
        total = result_json['total']
        assert int(total) > 1000
        data = result_json['data']
        for unit in data:
            self.xiaoguotu_ids.append(unit['ID'])
        xiaoguotu_links = ['http://exh.zhankoo.com/xiaoguotu/{}.html'.format(str(i)) for i in self.xiaoguotu_ids]
        open_links(xiaoguotu_links, self.xiaoguotu_links_error)

    def test_zhanguan(self):
        '''获取展馆首页数据,并打开展馆详情页'''

        for i in range(1, 9):
            zhanguan_links = []
            data = {
                'pageIndex': 1,
                'pageSize': 10,
                'type': i
            }
            web_response = requests.post(self.zhanguan_data_url, data=data)
            soup = BeautifulSoup(web_response.text, 'lxml')
            targets = soup.select('li.clearfix > div.pic.fl > a')
            for target in targets:
                zhanguan_links.append('http://exh.zhankoo.com' + target.get('href'))
            assert len(zhanguan_links) > 0
            try:
                for link in zhanguan_links:
                    open(link)
            except Exception:
                self.zhanguan_links_error.append(link)
        if len(self.zhanguan_links_error) != 0:
            print(self.zhanguan_links_error)
            assert False

    def test_txzhanshang(self):
        '''测试天下展商首页数据，并打开详情页'''
        data1 = {
            'archileLocationCode': 'Txzhanshang',
            'extArchileLocationCode':"'NewsFlash_Txzhanshang','Cx_Txzhanshang_xwdsr','Cx_Txzhanshang_qys','Cx_Txzhanshang_dks','Cx_Txzhanshang_mtjj','G20_Txzhanshang_Toutiao','G20_Txzhanshang_Depth','G20_Txzhanshang_LastNews','G20_Txzhanshang_Comment','G20_Txzhanshang_Talk','G20_Txzhanshang_SecrectNews','G20_Txzhanshang_Notes','NewsConference_Txzhanshang_Media','NewsConference_Txzhanshang_Sets','NewsConference_Txzhanshang_Work','NewsConference_Txzhanshang_Watch','NewsConference_Txzhanshang_Top','GuoQing_Txzhanshang_House','GuoQing_Txzhanshang_Car','GuoQing_Txzhanshang_Game','GuoQing_Txzhanshang_Floor','GuoQing_Txzhanshang_Forgain','GuoQing_Txzhanshang_Other','GJH_Txzhanshang_FocuNews','GJH_Txzhanshang_FuncChange','GJH_Txzhanshang_Zhaoshang','GJH_Txzhanshang_SecrectNews','GJH_Txzhanshang_Chuzheng','GJH_Txzhanshang_History','GJH_Txzhanshang_Comment','GaoJH_Txzhashang_Focus','GaoJH_Txzhashang_On','GaoJH_Txzhashang_Exhibitor','GaoJH_Txzhashang_Popular','GaoJH_Txzhashang_Guide','GaoJH_Txzhashang_Booth','GaoJH_Txzhashang_Other','GaoJH_Txzhashang_Events'",
            'pageIndex': 1,
            'pageSize': 20,
            'type': 1,
            'menuIndex': 1
        }
        data2 = {
            'archileLocationCode': 'Txzhanshang_Special',
            'pageIndex': 1,
            'pageSize': 20,
            'type': 2,
            'menuIndex': 2
        }
        data3 = {
            'archileLocationCode': 'Txzhanshang_Depth',
            'pageIndex': 1,
            'pageSize': 20,
            'type': 2,
            'menuIndex': 3
        }
        data4 = {
            'archileLocationCode': 'Txzhanshang_Image',
            'pageIndex': 1,
            'pageSize': 20,
            'type': 2,
            'menuIndex': 4
        }
        data5 = {
            'archileLocationCode': 'Txzhanshang_Character',
            'pageIndex': 1,
            'pageSize': 20,
            'type': 2,
            'menuIndex': 5
        }
        datas = [data1, data2, data3, data4, data5]
        for data in datas:
            txzhanshang_ids = []
            txzhanshang_links = []
            error_links = []
            web_response = requests.post(self.txzhanshang_data_url, data=data)
            dr = re.compile(r'<[^>]+>|\\r\\n', re.S)
            dd = dr.sub('', web_response.text)
            count = int(json.loads(dd)['totalCount'])
            assert count > 0
            res = '{"res":' + json.loads(dd)['archiles'] + "}"
            for item in json.loads(res)['res']:
                txzhanshang_ids.append(item['ID'])
            for id in txzhanshang_ids:
                txzhanshang_ids.append('http://txzhanshang.zhankoo.com/detail/%s.html' % id)
            open_links(txzhanshang_links, error_links)




