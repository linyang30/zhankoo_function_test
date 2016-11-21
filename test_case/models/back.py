import requests
import json

class Back:

    back_zhanwei_requirement_url = 'http://back.zhankoo.com/Exhibition/Booth/BoothBookFindPaged'
    back_del_zhanwei_requirement_url = 'http://back.zhankoo.com/Exhibition/Booth/BoothBookDelete'
    back_zhanzhuang_requirement_url = 'http://back.zhankoo.com/Exhibition/Decorate/DecorateBookFindPaged'
    back_del_zhanzhuang_requirement_url = 'http://back.zhankoo.com/Exhibition/Decorate/DecorateBookDelete'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0',
        'Cookie': 'pgv_pvi=5899286528; Hm_lvt_eb7b96a72f37b30dd098bacbb7e63b84=1477290116,1477626020,1478141069; Hm_lvt_c9f4a5eab06364796310e6b7a7033ba8=1477290115,1477626020,1478141069; ASP.NET_SessionId=sxaqaqbjbiuz3qoc3pduau0n; .ApplicationCookie=DB10DA4092558E126CDE47BCFF7D907EF90D4867D1A0AFE686EDC7E40CB90BFAB7ADAAD879A922AC64669836A131F318CA02F93148F25A8F24E369CB1B17E6B6450450F31BE17A3D9059278A1369F351ED0686459264A270A930AD0EA32EDA3A86642F7BEE4B2ED7009EA39D88D96D2D16C78E48F638AF393E3E2CEDAFC4CE4847B39D23ED33B080F3133C8AE3B45FE20179A7C966600BC9FFB0E45B739373A6B2CFD59E033979A857CE3390200675DA3E3DD7547B5BB4668A25FF7E5CC9B1EBF7FEE95D4985FCBEFDA5136C753C1CCAA14EA429'
    }

    def find_lastest_requirement(self, is_zhanwei):
        data = {
            'page': 1,
            'rows': 1,
            'sort': 'CreateOn',
            'order': 'DESC'
        }
        if is_zhanwei:
            url = self.back_zhanwei_requirement_url
        else:
            url = self.back_zhanzhuang_requirement_url
        web_response_back = requests.post(url, headers=self.headers, data=data)
        res = json.loads(web_response_back.text)['rows'][0]['ID']
        return res

    def del_requirement(self, id, is_zhanwei):
        data = {
            'id': id
        }
        if is_zhanwei:
            url = self.back_del_zhanwei_requirement_url
        else:
            url = self.back_del_zhanzhuang_requirement_url
        web_response = requests.post(url, headers=self.headers, data=data)
        res = json.loads(web_response.text)['success']
        assert res == True
