from models.zhanzhuang_ordering_process import *
from models.back import Back
import unittest
import random


class ZhanzhuangOrderingProcessTest(unittest.TestCase):

    def setUp(self):
        self.back = Back()
        self.require_title = '测试展装需求' + str(random.randint(100000, 999999))

    def test_zhanzhuang_ordering_process_online(self):
        '''展装在线订单'''
        submit_zhanzhuang_requirement()
        id = get_lastest_zhanzhuang_require_id()
        self.back.confirm_zhanzhuang_requirement(id, self.require_title)
        self.back.matching_company(id)
        distribute_id = self.back.get_distribute_id(id)
        self.back.price_insert(id, distribute_id, 'false')
        self.back.comfirm_price(id)
        order_save(id)

    def test_zhanzhuang_ordering_process_offline(self):
        '''展装离线订单'''
        submit_zhanzhuang_requirement()
        id = get_lastest_zhanzhuang_require_id()
        self.back.confirm_zhanzhuang_requirement(id, self.require_title)
        self.back.matching_company(id)
        distribute_id = self.back.get_distribute_id(id)
        self.back.price_insert(id, distribute_id, 'true')
        self.back.comfirm_price(id)
        order_id = order_save(id)
        offine_order_confirm_payment(order_id, 1)
        order_prepare(order_id)
        offine_order_confirm_payment(order_id, 2)
        order_building(order_id)
        self.back.set_supervisor(order_id)
        path = supervisor_report_pic_upload('zhanhui.jpg')
        imgs = ',' + path
        supervisor_report_save(order_id,imgs)
        confirm_accept(order_id)

