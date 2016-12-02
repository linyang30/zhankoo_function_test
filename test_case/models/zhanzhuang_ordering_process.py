from models.get_session import get_front_session
import random
import json
from bs4 import BeautifulSoup
from models.back import Back
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder

canzhanshang = get_front_session('13500000018', '123456')
fuwushang = get_front_session('exService@zhankoo.com', '123456')
jianli = get_front_session('18165702771', '123456')
submit_zhanzhuang_requirement_url = 'http://exh.zhankoo.com/Decorate/Exhibitor/DecorateBookSave'
canzhanshang_zhanzhuang_requirement_list_url = 'http://exh.zhankoo.com/Decorate/Partial/_DecorateBookFindPage'
order_save_url = 'http://exh.zhankoo.com/Decorate/Exhibitor/SureOrderSave'
offline_order_confirm_payment_url = 'http://so.zhankoo.com/decorate/exhibitor/offlineorderconfirmpayment'
order_prepare_url = 'http://so.zhankoo.com/Decorate/Decorator/OrderPrepare'
order_building_url = 'http://so.zhankoo.com/Decorate/Decorator/OrderBuilding'
supervisor_report_pic_upload_url = 'http://so.zhankoo.com/Home/PictureSave'
supervisor_report_save_url = 'http://so.zhankoo.com/Decorate/Partial/OrderReportSave'
confirm_accept_url = 'http://so.zhankoo.com/Decorate/Exhibitor/ConfirmAccept'
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

def order_save(id):
    data = {
        'DecorateBookID': id,
        'InternatType': '86',
        'CountryName': '中国',
        'CountryCode': '86',
        'X-Requested-With': 'XMLHttpRequest'
    }
    web_response = canzhanshang.post(order_save_url, data=data)
    assert json.loads(web_response.text)['success']
    return json.loads(web_response.text)['orderID']

def offine_order_confirm_payment(order_id, index):
    '''
    index = 1 是首款
    index = 2 是尾款
    '''
    data = {
        'orderID': order_id,
        'index': index
    }
    web_response = canzhanshang.post(offline_order_confirm_payment_url, data=data)
    assert json.loads(web_response.text)['success']

def order_prepare(order_id):
    data = {
        'orderID': order_id
    }
    web_response = fuwushang.post(order_prepare_url, data=data)
    assert json.loads(web_response.text)['success']

def order_building(order_id):
    data = {
        'orderID': order_id
    }
    web_response = fuwushang.post(order_building_url, data=data)
    assert json.loads(web_response.text)['success']

def supervisor_report_pic_upload(filename):
    current = os.getcwd()
    base = current.split('\\test_case')[0]
    target = base + '\\data\\' + filename
    multipart_data = MultipartEncoder(
        fields={
            'image': (filename, open(target, 'rb'), 'image/jpeg'),
            'Width': '127',
            'Height': '80',
            'Prefix': 'supervisor',
            'CallBack': 'parent.OnCompleteUpload'
        }
    )

    header = {
        'Content-Type': multipart_data.content_type
    }

    web_response = jianli.post(supervisor_report_pic_upload_url, data=multipart_data, headers=header)
    result = json.loads(web_response.text.split('OnCompleteUpload')[1].split('catch(e)')[0][2:-4])
    assert result['success'] == True
    return result['pictureUrl']

def supervisor_report_save(order_id, imgs):
    data = {
        'DecorateOrderID': order_id,
        'ImgStr': imgs
    }
    web_response = jianli.post(supervisor_report_save_url, data=data)
    assert json.loads(web_response.text)['success']

def confirm_accept(order_id):
    data = {
        'orderID': order_id
    }
    web_response = canzhanshang.post(confirm_accept_url, data=data)
    assert json.loads(web_response.text)['success']





if __name__ == '__main__':
    submit_zhanzhuang_requirement()
    id = get_lastest_zhanzhuang_require_id()
    back.confirm_zhanzhuang_requirement(id, require_title)
    back.matching_company(id)
    distribute_id = back.get_distribute_id(id)
    back.price_insert(id, distribute_id)
    back.comfirm_price(id)