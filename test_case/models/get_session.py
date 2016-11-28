import requests
from bs4 import BeautifulSoup

login_page_url = 'http://passport.zhankoo.com/account/login/'
login_url = 'http://passport.zhankoo.com/Account/LoginAjax'
back_login_url = 'http://back.zhankoo.com/account/signin'


def get_login_token():
    web_response = requests.get(login_page_url)
    soup = BeautifulSoup(web_response.text, 'lxml')
    token = soup.find('input', attrs={'name': '__RequestVerificationToken'}).get('value')
    return token


def get_front_session(name, password):
    session = requests.session()
    token = get_login_token()
    data = {
        '__RequestVerificationToken': token,
        'LoginFailNum': 1,
        'Name': name,
        'Password': password,
        'VerifyCode': '',
        'RememberMe': 'false',
        'X-Requested-With': 'XMLHttpRequest'
    }
    session.post(login_url, data=data)
    return session
def get_back_session(name='admin_default@izhanxiao.com', password='zkadmin_987456'):
    session = requests.session()
    data = {
        'loginName': name,
        'password': password
    }
    session.post(back_login_url, data=data)
    return session