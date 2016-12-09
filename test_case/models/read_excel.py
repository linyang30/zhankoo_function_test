import xlrd
import os

def get_default_file_path():
    current_path = os.getcwd()
    base = current_path.split('\\test_case')[0]
    path = base + '\\data\\file.xlsx'
    return path

def open_excel(file):
    data = xlrd.open_workbook(file)
    return data

def excel_table_by_index(file = get_default_file_path(), by_index = 0):
    '''
    by_index = 0 用户登录测试数据
    by_index = 1 参展宝展会测试数据
    by_index = 2 参展宝展装测试数据
    '''
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    list1 = []
    for rownum in range(nrows):
        row = table.row_values(rownum)
        list1.append(row)
    return list1



if __name__ == '__main__':
    print(excel_table_by_index())