import unittest
from models.release_exhibition import ReleaseExhibition
import random
from models.back import Back

class ReleaseExhibtionTest(unittest.TestCase):

    def setUp(self):
        self.back = Back()

    def test_release_exhibition(self):

        release_exhibition = ReleaseExhibition()
        exhibition_name = '测试' + str(random.randint(10000, 99999))
        result = release_exhibition.release_exhibition_basic_info(exhibition_name)
        id = result['ID']
        assert result['success'] == True
        back_id = self.back.find_lastest(3)
        assert id == back_id
        release_exhibition.save_introduction(id, '展会介绍111111111111', '展览范围2222222222', '标签33333333')
        release_exhibition.institution_save(id, '主办机构11111111', '承办机构222222222')
        zhanwei_info = {
            'biaozhan_price': 5500,
            'biaozhan_area': 9,
            'biaozhan_shuoming': '什么都没有',
            'guangdi_price': 2000,
            'guangdi_area': 12,
            'guangdi_shuoming': '光地就是都没有'
        }
        release_exhibition.zhanwei_info_save(id, zhanwei_info)

        img1 = release_exhibition.pic_upload(1, 'img1.jpg')
        img2 = release_exhibition.pic_upload(1, 'img2.jpg')
        img3 = release_exhibition.pic_upload(1, 'img3.jpg')
        imgs = ',' + img1 + ',' + img2 + ',' + img3 + ','
        release_exhibition.exhibition_pic_save(imgs, id)

        meeting_url = release_exhibition.pic_upload(2, 'zhanhui.jpg')
        param = {
            'subject': '测试同期会议的主题',
            'start_time': '2017-08-08',
            'end_time': '2017-08-16',
            'address': '深圳市南山区源兴科技大厦',
            'organizer': '展酷网络科技',
            'max_people': 100,
            'img_url': meeting_url,
            'description': '测试同期展会'
        }
        release_exhibition.meeting_save(id, param)


        # self.back.del_item(id, 3)
