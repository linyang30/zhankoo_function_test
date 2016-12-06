from models.zhanhui_search import zhanhui_search
import unittest

class ZhanhuiSearchTest(unittest.TestCase):

    def test_zhanhui_search_success(self):
        zhanhui_search('机械', True)

    def test_zhanhui_search_fail(self):
        zhanhui_search('test', False)