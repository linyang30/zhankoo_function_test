import unittest
from models.can_zhan_bao import CanZhanBao
from models.back import Back


booking_zhanwei_insert_url = 'http://exh.zhankoo.com/Home/BoothBookInsert'
booking_zhanwei_supplement_url = 'http://exh.zhankoo.com/Home/BoothBookSupplement'
booking_zhanzhuang_insert_url = 'http://exh.zhankoo.com/Home/DecorateBookInsert'
booking_zhanzhuang_supplement_url = 'http://exh.zhankoo.com/Home/DecorateBookSupplement'
contact_name = 'Test_user'
phone_number = '18126127906'
from_site = 10
from_site_location = 'FromSiteLocation:Home_Index_TopLeft'
company_name = 'Test_company'
main_product = 'Test_product'
is_first_exhibit = 1
intent_city = 'Test_city'
time_on = '2017-10-01'
area = 9
intent_exhibit = 'Test_exhibit'
service_item = '会展设计'
exhibition_name = 'Test_exhibit'
budget = '2~3万'



class CanzhanbaoTest(unittest.TestCase):

    def setUp(self):
        self.can_zhan_bao = CanZhanBao()
        self.back = Back()

    def test_booking_zhanwei(self):
        '''提交展位需求'''
        booking_insert_param = {
            'contact_name': contact_name,
            'phone_number': phone_number,
            'from_site': from_site,
            'from_site_location': from_site_location,
            'url': booking_zhanwei_insert_url
        }
        id = self.can_zhan_bao.booking_insert(booking_insert_param)
        booking_supplement_param = {
            'is_zhanwei':True,
            'id': id,
            'company_name': company_name,
            'main_product': main_product,
            'is_first_exhibit': is_first_exhibit,
            'intent_city': intent_city,
            'exhibit_on': time_on,
            'require_area': area,
            'intent_exhibit': intent_exhibit,
            'url': booking_zhanwei_supplement_url
        }
        self.can_zhan_bao.booking_supplement(booking_supplement_param)
        res = self.back.find_lastest_requirement(is_zhanwei=True)
        assert id == res
        self.back.del_requirement(id, is_zhanwei=True)

    def test_booking_zhanzhuang(self):
        '''提交展装需求'''
        booking_insert_param = {
            'contact_name': contact_name,
            'phone_number': phone_number,
            'from_site': from_site,
            'from_site_location': from_site_location,
            'url': booking_zhanzhuang_insert_url
        }
        id = self.can_zhan_bao.booking_insert(booking_insert_param)
        booking_supplement_param = {
            'is_zhanwei': False,
            'id': id,
            'service_item': service_item,
            'exhibition_name': exhibition_name,
            'area': area,
            'finish_on': time_on,
            'budget': budget,
            'company_name': company_name,
            'intent_exhibit': intent_exhibit,
            'url': booking_zhanzhuang_supplement_url
        }
        self.can_zhan_bao.booking_supplement(booking_supplement_param)
        res = self.back.find_lastest_requirement(is_zhanwei=False)
        assert id == res
        self.back.del_requirement(id, is_zhanwei=False)



