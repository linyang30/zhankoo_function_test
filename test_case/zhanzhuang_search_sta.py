from models.zhanzhuang_search import zhanzhuang_search
import unittest


class ZhanzhuangSearchTest(unittest.TestCase):
     def test_zhanzhuang_search_success(self):
         zhanzhuang_search('风尚', True)

     def test_zhanzhuang_search_fail(self):
         zhanzhuang_search('test', False)