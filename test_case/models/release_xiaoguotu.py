from models.get_session import get_front_session
import os
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

class ReleaseXiaoguotu:

    session = get_front_session('exService@zhankoo.com', '123456')
    pic_save_url = 'http://exh.zhankoo.com/Home/PictureSave'

    def pic_upload(self, filename):
        current = os.getcwd()
        base = current.split('\\test_case')[0]
        target = base + '\\data\\' + filename
        multipart_data = MultipartEncoder(
            fields={
                'image': (filename, open(target, 'rb'), 'image/jpeg'),
                'Width': '460',
                'Height': '280',
            }
        )

        header = {
            'Content-Type': multipart_data.content_type
        }

        web_response = self.session.post(self.pic_save_url, data=multipart_data, headers=header)
        result = json.loads(web_response.text.split('zhankoo.com')[1].split('catch(e)')[0][5:-4])
        assert result['success'] == True
        return result['pictureUrl']


    def release_xiaoguotu(self):
        data = {

        }


if __name__ == '__main__':
    print(ReleaseXiaoguotu().pic_upload('zhanhui.jpg'))
