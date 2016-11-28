import requests
from bs4 import BeautifulSoup
import json
from models.get_session import get_front_session
import os

class ReleaseExhibition:

    basic_info_url = 'http://exh.zhankoo.com/Exhibition/Organizer/BasicSave'
    introduction_save_url = 'http://exh.zhankoo.com/Exhibition/Organizer/IntroductionSave'
    institution_save_url = 'http://exh.zhankoo.com/Exhibition/Organizer/InstitutionSave'
    zhanwei_info_save_url = 'http://exh.zhankoo.com/Exhibition/Organizer/BasicBoothSave'
    exhibition_pic_upload_url = 'http://exh.zhankoo.com/Exhibition/Organizer/ExPictureSave'
    exhibition_pic_save_url = 'http://exh.zhankoo.com/Exhibition/Organizer/PictureSave'
    meeting_pic_upload_url = 'http://exh.zhankoo.com/Exhibition/Organizer/MeetingPictureSave'
    meeting_save_url = 'http://exh.zhankoo.com/Exhibition/Organizer/MeetingSave'

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Cookie': 'pgv_pvi=7247156224; ASP.NET_SessionId=epd2nnxmw5sj3rcox2vuwv3o; pgv_si=s5272052736; Hm_lvt_c9f4a5eab06364796310e6b7a7033ba8=1479863530,1480035307,1480063675,1480295780; Hm_lpvt_c9f4a5eab06364796310e6b7a7033ba8=1480299848; Hm_lvt_eb7b96a72f37b30dd098bacbb7e63b84=1479863530,1480035308,1480063675,1480295780; Hm_lpvt_eb7b96a72f37b30dd098bacbb7e63b84=1480299848; .AspNet.ApplicationCookie=LsovQ8vtubsyvhcHRfFF5wjDpth-eerRWnpsmXdcSmWsuu-PZjDEA6bgoKeVz0fOXRVwuSfKMxXGxeAfVbOGVt4PZ4yqgz2a6C8RWt0bWEjJw2SXbR61BFx9hP67iXUSAXtXmjd-Lx65NDSaLkBwSHvfWaz-4M6V9c0f_ZkfJBvyVdIBRqia43eSKzObpakXqZyHMF-08UNk1WvKTAu5j2SXe_jqmgiRoxVr1AKKXEcDaZ9QpSsY0gb7sc1n3GhWW_tn4fG7k2s-vHpr9wKEa9365oyEQLVd2o3XhJ-RLnx3tGneN2Rwrc5M6XE0hYnGLBoj3sRSWIXyP6-yupLRAyDtSVBEZT5Dal0GNjWL2MwWDCavqF5We1ZfFb_uXQUvi9GlQA',
        'Referer': 'http://exh.zhankoo.com/exhibition/organizer/publish',
        'Origin': 'http://exh.zhankoo.com'
    }

    session = get_front_session('18320836325', '123456')

    def release_exhibition_basic_info(self, exhibition_name):
        data = {
            'ID': 0,
            'Name': exhibition_name,
            'ShortName': 'test',
            'IndustryName': 'IT通信',
            'IndustryID': 80,
            'ExhibitCategory': '[{"ID":3,"Name":"包装机械/塑料机械"},]',
            'HoldFrequencyWithYear': 1,
            'HoldFrequency': 1,
            'FromOn': '2017/12/22',
            'ToOn': '2017/12/24',
            'PavilionID': 3118,
            'PavilionName': '深圳会展中心',
            'Address': '中国广东深圳市福田区',
            'Site': 'www.zhankoo.com',
            'X-Requested-With': 'XMLHttpRequest'
        }
        # web_response = requests.post(self.basic_info_url, headers=self.header, data=data)
        web_response = self.session.post(self.basic_info_url, data=data)
        soup = BeautifulSoup(web_response.text, 'lxml')
        return json.loads(soup.select('html > body > p')[0].get_text())

    def save_introduction(self, id, description, scope, tag):
        data = {
            'ID': id,
            'Description': description,
            'Scope': scope,
            'Tag': tag
        }
        # web_response = requests.post(self.introduction_save_url, headers=self.header, data=data)
        web_response = self.session.post(self.introduction_save_url, data)
        assert json.loads(web_response.text)['success']

    def institution_save(self, id, organizer, contractor):
        data = {
            'ID': id,
            'Organizer': organizer,
            'Contractor': contractor
        }
        # web_response = requests.post(self.institution_save_url, headers=self.header, data=data)
        web_response = self.session.post(self.institution_save_url, data=data)
        assert json.loads(web_response.text)['success']

    def zhanwei_info_save(self, id, param):
        orderJson = [
            {"Type":1,
             "Price":param['biaozhan_price'],
             "Area": param['biaozhan_area'],
             "Description":param['biaozhan_shuoming']},

                     {"Type":2,
                      "Price":param['guangdi_price'],
                      "Area":param['guangdi_area'],
                      "Description":param['guangdi_shuoming']}
                    ]
        data = {
            'ID': id,
            'MinOrderJson': str(orderJson),
            'StandardBoothMoney': param['biaozhan_price'],
            'StandardBoothArea': param['biaozhan_area'],
            'StandardBoothRemark': param['biaozhan_shuoming'],
            'BareSpaceBoothMoney': param['guangdi_price'],
            'BareSpaceBoothArea': param['guangdi_area'],
            'BareSpaceBoothRemark': param['guangdi_shuoming'],
            'X-Requested-With': 'XMLHttpRequest'
        }
        web_response = self.session.post(self.zhanwei_info_save_url, data=data)
        assert json.loads(web_response.text)['success']

    def pic_upload(self, type, filename):
        '''
        1: 上传展会图片
        2: 上传同期会议图片
        '''
        current = os.getcwd()
        base = current.split('\\test_case')[0]
        target = base + '\\data\\' + filename
        files = {'file': open(target, 'rb')}
        url = ''
        if type == 1:
            url = self.exhibition_pic_upload_url
        elif type == 2:
            url = self.meeting_pic_upload_url
        web_response = self.session.post(url, files=files)
        result = ''
        if type == 1:
            result = json.loads(web_response.text.split('OnCompleteUpload')[1].split('catch(e)')[0][2:-4])
        elif type == 2:
            result = json.loads(web_response.text.split('MeetingComplete')[1].split('catch(e)')[0][2:-4])
        assert result['success'] == True
        return result['pictureUrl']

    def exhibition_pic_save(self, imgs, id):
        data = {
            'ImgStr': imgs,
            'ID': id
        }
        web_response = self.session.post(self.exhibition_pic_save_url, data=data)
        assert json.loads(web_response.text)['success']

    def meeting_save(self, id, param):
        data = {
            'ID': '',
            'ExhibitionID': id,
            'Name': param['subject'],
            'MeetingFromOn': param['start_time'] + ' 00:00',
            'MeetingToOn': param['end_time'] + ' 00:00',
            'Address': param['address'],
            'Organizer': param['organizer'],
            'MaxPeople': param['max_people'],
            'ImageUrl': param['img_url'],
            'Description': param['description'],
            'X-Requested-With': 'XMLHttpRequest'
        }
        web_response = self.session.post(self.meeting_save_url, data=data)
        assert json.loads(web_response.text)['success']

if __name__ == '__main__':
    print(ReleaseExhibition().pic_upload('zhanhui.jpg'))