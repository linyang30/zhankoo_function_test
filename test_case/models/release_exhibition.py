import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode

class ReleaseExhibition:

    basic_info_url = 'http://exh.zhankoo.com/Exhibition/Organizer/BasicSave'
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Cookie': 'pgv_pvi=7247156224; ASP.NET_SessionId=14tyjtn3s5d5z2aozlyrthud; pgv_si=s2853089280; Hm_lvt_c9f4a5eab06364796310e6b7a7033ba8=1479690583,1479709778,1479776849,1479863530; Hm_lpvt_c9f4a5eab06364796310e6b7a7033ba8=1479969662; Hm_lvt_eb7b96a72f37b30dd098bacbb7e63b84=1479690584,1479709778,1479776850,1479863530; Hm_lpvt_eb7b96a72f37b30dd098bacbb7e63b84=1479969663; .AspNet.ApplicationCookie=Tvf_3AB-LTtrdBwsBo8_rgOMi91Mu7TKx3Z0zaR7GnVB4g1Q8jCNVvrwA1mkf9Tvo0PMzTRO6veHonn6BrP0WSYOekSugLar0_B13D4oi6AFO6YEE1er91lwiJ_lMkCAcQjAnBWGCYtYgcyX2lGqg6gzL6_LciJe80nDTnuSo2yYy0N6sliJJybEPEDG1vBSEjjZLf294Fs7QcK8do7ePdI4BsJ6xrNj08OPSW7xPlyQXk65wi1bcpJtClN-Hg8iBDPvbxo3jZAozGGC0LgseMzcwgH-u4tMpgnbO2qUjtZNwCyu4BjuNvPY3va-HqhaogKmW6yLpG5c9Lz0D9k9AC5wADRCywKXXfICTUsZDSY0tVtYBRiCZrISAxnLx-EH2j_BYA',
        'Referer': 'http://exh.zhankoo.com/exhibition/organizer/publish'
    }

    def release_exhibition_basic_info(self, exhibition_name):
        data = {
            'ID': 0,
            'Name': exhibition_name,
            'ShortName': 'Test_exhibition_short_name',
            'IndustryName': '',
            'IndustryID': 80,
            'ExhibitCategory': '[{"ID":3,"Name":"包装机械/塑料机械"},]',
            'HoldFrequencyWithYear': 1,
            'HoldFrequency': 1,
            'FromOn': '2017/12/22',
            'ToOn': '2017/12/24',
            'PavilionID': 3118,
            'PavilionName': '深圳会展中心',
            'Address': '中国广东深圳市福田区',
            'Site': 'http://www.zhankoo.com',
            'X-Requested-With': 'XMLHttpRequest'
        }
        #data = urlencode(data)
        web_response = requests.post(self.basic_info_url, headers=self.header, data=data)
        soup = BeautifulSoup(web_response.text, 'lxml')
        print(soup)
if __name__ == '__main__':
    ReleaseExhibition().release_exhibition_basic_info('测试展会11245')