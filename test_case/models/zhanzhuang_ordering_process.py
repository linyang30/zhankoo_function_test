from models.get_session import get_front_session
import random
import json
from bs4 import BeautifulSoup
from models.back import Back

canzhanshang = get_front_session('13500000018', '123456')
submit_zhanzhuang_requirement_url = 'http://exh.zhankoo.com/Decorate/Exhibitor/DecorateBookSave'
canzhanshang_zhanzhuang_requirement_list_url = 'http://exh.zhankoo.com/Decorate/Partial/_DecorateBookFindPage'
back = Back()
require_title = '测试展装需求' + str(random.randint(100000, 999999))

def submit_zhanzhuang_requirement():
    data = {
        'FromSite': 10,
        'FromSiteLocation': '//exh.zhankoo.com/_Decorate_Exhibitor_DecorateBookCreate_Index',
        'Subject': require_title,
        'ExhibitorEnterpriseID': 485,
        'ExhibitorEnterpriseName': '深圳展酷网络有限公司',
        'ContactIDs': 134745,
        'ProvinceName': '广东省',
        'CityName': '深圳市',
        'ExhibitionID': 20159,
        'ExhibitionName': '测试90761',
        'BoothID': 55471,
        'BoothName': 'zhanwei109',
        'ServiceItem': '会展设计',
        'ProvinceCode': 440000,
        'CityCode': 440300,
        'FinishOn': '2017/02/15',
        'DesignerDemand': '设计师需求',
        'DecorateDemand': '展装需求',
        'X-Requested-With': 'XMLHttpRequest'
    }
    web_response = canzhanshang.post(submit_zhanzhuang_requirement_url, data=data)
    assert json.loads(web_response.text)['success']

def get_lastest_zhanzhuang_require_id():
    web_response = canzhanshang.get(canzhanshang_zhanzhuang_requirement_list_url)
    soup = BeautifulSoup(web_response.text, 'lxml')
    id = soup.select('body a')[0].get_text()
    return id




if __name__ == '__main__':
    submit_zhanzhuang_requirement()
    id = get_lastest_zhanzhuang_require_id()
    back.confirm_zhanzhuang_requirement(id, require_title)