from HTMLTestRunner import HTMLTestRunner
import time
import os
import unittest




if __name__ == '__main__':
    now = time.strftime('%Y_%m_%d')
    base_dir = os.getcwd()
    base = base_dir.split('\\test_case')[0]
    filename = base + '\\report\\' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='展酷网自动化测试报告', description='环境：win7')
    discover = unittest.defaultTestLoader.discover(base + '\\test_case',pattern='*_sta.py')
    runner.run(discover)
    fp.close()

