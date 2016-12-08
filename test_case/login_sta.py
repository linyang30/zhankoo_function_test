import unittest
from models.login import Login
from models.read_excel import excel_table_by_index
from models.get_session import get_front_session
from bs4 import BeautifulSoup


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.login = Login()

    def test_login_no_username_and_password(self):
        '''当用户名和密码都为空时登陆'''
        result_list = self.login.get_login_error_message()
        assert set(['请输入手机号/邮箱', '请输入密码']).issubset(set(result_list))

    def test_login_no_password(self):
        '''当密码为空时登陆'''
        result_list = self.login.get_login_error_message(name='13500000018')
        assert set(['请输入密码']).issubset(set(result_list))

    def test_login_no_username(self):
        '''当用户名为空时登陆'''
        result_list = self.login.get_login_error_message(password='123456')
        assert set(['请输入手机号/邮箱']).issubset(set(result_list))

    def test_login_error_password(self):
        '''当密码错误时登陆'''
        result = self.login.send_login_request(name='13500000018', password='654321')
        assert result['success'] == False

    def test_login_error_username(self):
        '''当用户名错误时登陆'''
        result = self.login.send_login_request(name='13500000017', password='123456')
        assert result['success'] == False

    def test_login_character(self):
        '''测试各种用户角色登陆'''
        user_list = excel_table_by_index()
        for user in user_list:
            try:
                username = int(user[0])
            except:
                username = user[0]
            try:
                password = int(user[1])
            except:
                password = user[1]
            character = user[2]
            session = get_front_session(username, password)
            web_response = session.get('http://www.zhankoo.com')
            soup = BeautifulSoup(web_response.text, 'lxml')
            result = soup.select('div.toolbar em')[0].get_text()
            assert result == character



