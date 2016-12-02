from models.get_session import get_front_session
import json
from bs4 import BeautifulSoup


canzhanshang = get_front_session('13500000018', '123456')
zhubanfang = get_front_session('18320836325', '123456')
canzhanshang_get_ticket_url = 'http://exh.zhankoo.com/Exhibition/Home/ActivityRegisterSave'
ticket_page_apply_url = 'http://exh.zhankoo.com/Exhibition/Partial/_OrganizerTicketPage'
confirm_ticket_pass_url = 'http://exh.zhankoo.com/Exhibition/Organizer/UpdateTicketPass'
confirm_ticket_unpass_url = 'http://exh.zhankoo.com/Exhibition/Organizer/UpdateTicketUnPass'


def canzhanshang_get_ticket():
    data = {
        'ExhibitionID': '20159',
        'TicketActiveID': '8131',
        'TicketName': '测试90761',
        'FromOn': '2017/12/22 0:00:00',
        'ToOn': '2017/12/24 0:00:00',
        'OrganizorID': '12876121',
        'RealName': '参展商',
        'EnterpriseName': 'test',
        'Title': 'test',
        'X-Requested-With': 'XMLHttpRequest'
    }
    web_response = canzhanshang.post(canzhanshang_get_ticket_url, data=data)
    assert json.loads(web_response.text)['success']

def get_ticket_apply_id():
    data = {
        'pageIndex': 1,
        'pageSize': 20,
        'State': '所有状态'
    }
    web_response = zhubanfang.post(ticket_page_apply_url, data=data)
    soup = BeautifulSoup(web_response.text, 'lxml')
    return soup.select('div.listtd tr')[1].get('applyid')

def confirm_ticket_pass(apply_id, reason):
    data = {
        'ticketID': apply_id,
        'checkOpinion': reason
    }
    web_response = zhubanfang.post(confirm_ticket_pass_url, data=data)
    assert json.loads(web_response.text)['success']

def confirm_ticket_unpass(apply_id, reason):
    data = {
        'ticketID': apply_id,
        'checkOpinion': reason
    }
    web_response = zhubanfang.post(confirm_ticket_unpass_url, data=data)
    assert json.loads(web_response.text)['success']

if __name__ == '__main__':
    canzhanshang_get_ticket()
    print(get_ticket_apply_id())
