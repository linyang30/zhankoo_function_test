from models.open_page import open, open_links
import unittest

class ChannelPage(unittest.TestCase):

    links_error = []

    channels = '''
        http://www.zhankoo.com
        http://www.zhankoo.com/zhanhui
        http://www.zhankoo.com/zhanzhuang
        http://exh.zhankoo.com/xiaoguotu
        http://www.zhankoo.com/zhanguan
        http://txzhanshang.zhankoo.com/
        http://www.zhankoo.com/baike
        http://exh.zhankoo.com/zhanzhuang/search
        http://exh.zhankoo.com/zhanhui/search
        http://www.zhankoo.com/baike/zh
        http://www.zhankoo.com/baike/zz
        http://www.zhankoo.com/baike/gc
        http://www.zhankoo.com/baike/bd
        http://www.zhankoo.com/baike/mj
        http://www.zhankoo.com/baike/zx
        '''



    def test_open_channel_page(self):
        '''打开所有频道页'''
        open_links(self.channels.split(), self.links_error)

