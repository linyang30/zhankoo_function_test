import requests
import json
from models.get_session import get_back_session

class Back:

    back_zhanwei_requirement_url = 'http://back.zhankoo.com/Exhibition/Booth/BoothBookFindPaged'
    back_del_zhanwei_requirement_url = 'http://back.zhankoo.com/Exhibition/Booth/BoothBookDelete'
    back_zhanzhuang_requirement_url = 'http://back.zhankoo.com/Exhibition/Decorate/DecorateBookFindPaged'
    back_zhanhui_url = 'http://back.zhankoo.com/Exhibition/Exhibition/ExhibitionFindPaged'
    back_del_zhanzhuang_requirement_url = 'http://back.zhankoo.com/Exhibition/Decorate/DecorateBookDelete'
    back_del_zhanhui_url = 'http://back.zhankoo.com/Exhibition/Exhibition/ExhibitionDelete'
    back_decorate_case_url = 'http://back.zhankoo.com/Exhibition/Decorate/DecorateCaseFindPaged'
    back_del_decorate_case_url = 'http://back.zhankoo.com/Exhibition/Decorate/DecorateCaseDelete'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0',
        'Cookie': 'pgv_pvi=5899286528; Hm_lvt_eb7b96a72f37b30dd098bacbb7e63b84=1477626020,1478141069,1479972174,1480040467; Hm_lvt_c9f4a5eab06364796310e6b7a7033ba8=1477626020,1478141069,1479972174,1480040467; ASP.NET_SessionId=kh0ufne3hepzhfab4yvqrabq; .ApplicationCookie=36F53D4975163D6F896A00EBBCE727833D2D16BF6DA2A7923270E01B2CB8BF61C27ADC54A9554897D6DF4C2A853C26C65B6A2D0F265B6AD595BFE5E5BE25245FB8B679A73751CEDFE5D11B3EF6699800B382CCCE7F4B1D4E74B7972FC3A72210379A1D05666C4CA5BE775526109D7057E1FD5C64C069D20710C3B0EB20F84D41799092CCC86C6F59AF952310AA6BD16C5C406E1E9B62757E843571B30A552A1F6D578D5683DC5C538BA392297C63DFFD9E836425A7F8075AA0A46559728AA5A3009E918BB399163A61F208D9F4CB09B06F543A5A'
    }

    '''
    1: 展位需求
    2：展装需求
    3：展会
    4: 展装效果图
    '''
    session = get_back_session()

    def find_lastest(self, code):
        data = {
            'page': 1,
            'rows': 1,
            'sort': 'CreateOn',
            'order': 'DESC'
        }
        if code == 1:
            url = self.back_zhanwei_requirement_url
        elif code == 2:
            url = self.back_zhanzhuang_requirement_url
        elif code == 3:
            url = self.back_zhanhui_url
        elif code == 4:
            url = self.back_decorate_case_url
        # web_response_back = requests.post(url, headers=self.headers, data=data)
        web_response_back = self.session.post(url, data=data)
        res = json.loads(web_response_back.text)['rows'][0]['ID']
        return res

    def del_item(self, id, code):
        data = {
            'id': id
        }
        if code == 1:
            url = self.back_del_zhanwei_requirement_url
        elif code == 2:
            url = self.back_del_zhanzhuang_requirement_url
        elif code == 3:
            url = self.back_del_zhanhui_url
        elif code == 4:
            url = self.back_del_decorate_case_url
        # web_response = requests.post(url, headers=self.headers, data=data)
        web_response = self.session.post(url, data=data)
        res = json.loads(web_response.text)['success']
        assert res == True
