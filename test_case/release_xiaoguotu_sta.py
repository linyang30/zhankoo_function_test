from models.release_xiaoguotu import ReleaseXiaoguotu
import unittest
import random
from models.back import Back


class ReleaseXiaoguotuTest(unittest.TestCase):

    def setUp(self):
        self.release_xiaoguotu = ReleaseXiaoguotu()
        self.back = Back()

    def test_release_xiaoguotu(self):
        path1 = self.release_xiaoguotu.pic_upload('img1.jpg')
        path2 = self.release_xiaoguotu.pic_upload('img2.jpg')
        path3 = self.release_xiaoguotu.pic_upload('img3.jpg')
        imgs = ',' + path1 + ',' + path2 + ',' + path3
        param = {
            'title': '测试效果图' + str(random.randint(10000, 99999)),
            'description': '测试说明',
            'industry_name': '房产家居',
            'industry_id': '103',
            'area': 9,
            'standard_type': 1,
            'material': '木质材质',
            'type': '简约',
            'price': 12000,
            'order': 1,
            'color': '白色',
        }
        self.release_xiaoguotu.release_xiaoguotu(imgs, param)
