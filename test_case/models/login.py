import requests
from bs4 import BeautifulSoup
import json


class Login:
    login_page_url = 'http://passport.zhankoo.com/account/login/'
    login_url = 'http://passport.zhankoo.com/Account/LoginAjax'

    def get_login_token(self):
        web_response = requests.get(self.login_page_url)
        soup = BeautifulSoup(web_response.text, 'lxml')
        token = soup.find('input', attrs={'name': '__RequestVerificationToken'}).get('value')
        return token

    def send_login_request(self, name, password):
        token = self.get_login_token()
        data = {
            '__RequestVerificationToken': token,
            'LoginFailNum': 1,
            'Name': name,
            'Password': password,
            'VerifyCode': '',
            'RememberMe': 'false',
            'X-Requested-With': 'XMLHttpRequest'
        }
        web_response = requests.post(self.login_url, data=data)
        soup = BeautifulSoup(web_response.text, 'lxml')
        result = soup.select('body > p')[0].get_text()
        return json.loads(result)['success']
