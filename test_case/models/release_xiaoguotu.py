from models.get_session import get_front_session
import os
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

class ReleaseXiaoguotu:

    session = get_front_session('exService@zhankoo.com', '123456')
    pic_save_url = 'http://exh.zhankoo.com/Home/PictureSave'
    decorate_case_save_url = 'http://exh.zhankoo.com/Decorate/Decorator/DecorateCaseSave'

    def pic_upload(self, filename):
        current = os.getcwd()
        base = current.split('\\test_case')[0]
        target = base + '\\data\\' + filename
        multipart_data = MultipartEncoder(
            fields={
                'image': (filename, open(target, 'rb'), 'image/jpeg'),
                'Width': '460',
                'Height': '280',
                'Index': '3',
                'Prefix': 'EnterpriseStyle',
                'CallBack': 'parent.OnComplete'
            }
        )

        header = {
            'Content-Type': multipart_data.content_type
        }

        web_response = self.session.post(self.pic_save_url, data=multipart_data, headers=header)
        # print(web_response.text)
        result = json.loads(web_response.text.split('OnComplete')[1].split('catch(e)')[0][2:-4])
        assert result['success'] == True
        return result['pictureUrl']


    def release_xiaoguotu(self, imgs, param):
        data = {
            'ID': '',
            'Title': param['title'],
            'Description': param['description'],
            'IndustryName': param['industry_name'],
            'IndustryID': param['industry_id'],
            'Area': param['area'],
            'BoothStandardType': param['standard_type'],
            'Material': param['material'],
            'Style': param['type'],
            'DesignerID': 1220,
            'Price': param['price'],
            'Order': param['order'],
            'colorAddId': param['color'],
            'Color': param['color'],
            'DecorateCaseImage': imgs,
            'X-Requested-With': 'XMLHttpRequest'
        }
        web_response = self.session.post(self.decorate_case_save_url, data=data)
        assert json.loads(web_response.text)['success']


if __name__ == '__main__':
    print(ReleaseXiaoguotu().pic_upload('zhanhui.jpg'))
