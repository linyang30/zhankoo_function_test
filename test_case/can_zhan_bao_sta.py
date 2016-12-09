import unittest
from models.can_zhan_bao import CanZhanBao
from models.back import Back
from models.read_excel import excel_table_by_index


booking_zhanwei_insert_url = 'http://exh.zhankoo.com/Home/BoothBookInsert'
booking_zhanwei_supplement_url = 'http://exh.zhankoo.com/Home/BoothBookSupplement'
booking_zhanzhuang_insert_url = 'http://exh.zhankoo.com/Home/DecorateBookInsert'
booking_zhanzhuang_supplement_url = 'http://exh.zhankoo.com/Home/DecorateBookSupplement'

class CanzhanbaoTest(unittest.TestCase):

    def setUp(self):
        self.can_zhan_bao = CanZhanBao()
        self.back = Back()

    def test_booking_zhanwei(self):
        '''提交展位需求'''
        zhanwei_data_list = excel_table_by_index(by_index=1)
        for zhanwei_data in zhanwei_data_list[1:]:
            try:
                area = int(zhanwei_data[9])
            except:
                area = zhanwei_data[9]

            booking_insert_param = {
                'contact_name': zhanwei_data[0],
                'phone_number': int(zhanwei_data[1]),
                'from_site': int(zhanwei_data[2]),
                'from_site_location': zhanwei_data[3],
                'url': booking_zhanwei_insert_url
            }
            id = self.can_zhan_bao.booking_insert(booking_insert_param)
            booking_supplement_param = {
                'is_zhanwei':True,
                'id': id,
                'company_name': zhanwei_data[4],
                'main_product': zhanwei_data[5],
                'is_first_exhibit': int(zhanwei_data[6]),
                'intent_city': zhanwei_data[7],
                'exhibit_on': zhanwei_data[8],
                'require_area': area,
                'intent_exhibit': zhanwei_data[10],
                'url': booking_zhanwei_supplement_url
            }
            self.can_zhan_bao.booking_supplement(booking_supplement_param)
            res = self.back.find_lastest(1)
            assert id == res
            self.back.del_item(id, 1)

    def test_booking_zhanzhuang(self):
        '''提交展装需求'''
        zhanzhuang_data_list = excel_table_by_index(by_index=2)
        for zhanzhuang_data in zhanzhuang_data_list[1:]:
            booking_insert_param = {
                'contact_name': zhanzhuang_data[0],
                'phone_number': int(zhanzhuang_data[1]),
                'from_site': int(zhanzhuang_data[2]),
                'from_site_location': zhanzhuang_data[3],
                'url': booking_zhanzhuang_insert_url
            }
            id = self.can_zhan_bao.booking_insert(booking_insert_param)
            booking_supplement_param = {
                'is_zhanwei': False,
                'id': id,
                'service_item': zhanzhuang_data[4],
                'exhibition_name': zhanzhuang_data[5],
                'area': int(zhanzhuang_data[6]),
                'finish_on': zhanzhuang_data[7],
                'budget': zhanzhuang_data[8],
                'company_name': zhanzhuang_data[9],
                'url': booking_zhanzhuang_supplement_url
            }
            self.can_zhan_bao.booking_supplement(booking_supplement_param)
            res = self.back.find_lastest(2)
            assert id == res
            self.back.del_item(id, 2)



