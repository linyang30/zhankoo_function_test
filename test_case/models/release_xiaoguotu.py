from models.get_session import get_front_session
import os
import json
import requests

class ReleaseXiaoguotu:

    session = get_front_session('exService@zhankoo.com', '123456')
    pic_save_url = 'http://exh.zhankoo.com/Home/PictureSave'

    def pic_upload(self, filename):
        current = os.getcwd()
        base = current.split('\\test_case')[0]
        target = base + '\\data\\' + filename
        files = {'file': open(target, 'rb')}
        web_response = self.session.post(self.pic_save_url, files=files)
        print(web_response.text)
        result = json.loads(web_response.text.split('OnCompleteUpload')[1].split('catch(e)')[0][2:-4])
        assert result['success'] == True
        return result['pictureUrl']


    def release_xiaoguotu(self):
        data = {

        }


if __name__ == '__main__':
    print(ReleaseXiaoguotu().pic_upload('zhanhui.jpg'))
