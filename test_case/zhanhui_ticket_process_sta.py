from models.zhanhui_ticket import *
from models.back import Back
import unittest


class ZhanhuiTicketTest(unittest.TestCase):

    def setUp(self):
        self.back = Back()

    def test_get_ticket_success(self):
        '''测试索票成功'''
        canzhanshang_get_ticket()
        apply_id = get_ticket_apply_id()
        confirm_ticket_pass(apply_id, '通过')
        back_id = self.back.find_lastest(5)
        assert str(apply_id) == str(back_id)
        self.back.del_item(apply_id, 5)

    def test_get_ticket_failed(self):
        '''测试索票失败'''
        canzhanshang_get_ticket()
        apply_id = get_ticket_apply_id()
        confirm_ticket_unpass(apply_id, '不通过')
        back_id = self.back.find_lastest(5)
        assert str(apply_id) == str(back_id)
        self.back.del_item(apply_id, 5)