import unittest
from models.login import Login


class LoginTest(unittest.TestCase):

    def test_login_success(self):
        '''测试登陆成功'''
        login = Login()
        result = login.send_login_request('13500000018', '123456')
        assert result == True

    def test_login_fail(self):
        '''测试登陆失败'''
        login = Login()
        result = login.send_login_request('13500000000', '123456')
        assert result == False