from test_case.models.open_page import open
import unittest

class MainPage(unittest.TestCase):

    main_page_url = 'http://www.zhankoo.com'

    def test_open_main_page(self):
        '''打开首页'''
        open(self.main_page_url)