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

        contact_save_info = {
            'contact': '林洋',
            'telephone': '0755-87654321',
            'mobile': '18126127906',
            'fax': '0755-12345678',
            'qq': '123456',
            'email': 'zhankoo@zhankoo.com'
        }
        release_exhibition.contact_save(id, contact_save_info)

        data_save_info = {
            'area': '1000',
            'net_area': '900',
            'history_num': '10',
            'viewer_quantity': '10000',
            'text_field1': '本地',
            'text_field2': '60',
            'text_field3': '外地',
            'text_field4': '40',
            'exhibition_quantity': '1000',
            'text_field5': '国内',
            'text_field6': '80',
            'text_field7': '国外',
            'text_field8': '20',
            'viewer_satisfy': '98',
            'exhibition_satisfy': '80',
        }
        release_exhibition.data_save(id, data_save_info)

        exbihitor_list = '展商1,展商2,展商3,展商4,展商5'
        release_exhibition.exhibitor_save(id, exbihitor_list)


        # self.back.del_item(id, 3)
