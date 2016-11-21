import requests
import json


class CanZhanBao:

    def booking_insert(self, param):

        data = {
            'Contact': param['contact_name'],
            'Mobile': param['phone_number'],
            'FromSite': param['from_site'],
            'FromSiteLocation': param['from_site_location']
        }

        web_response = requests.post(param['url'], data=data)
        res = json.loads(web_response.text)['success']
        assert res == True
        return json.loads(web_response.text)['id']

    def booking_supplement(self, param):
        if param['is_zhanwei']:
            data = {
                'ID': param['id'],
                'Enterprise': param['company_name'],
                'MainProduct': param['main_product'],
                'IsFirstExhibit': param['is_first_exhibit'],
                'IntentCity': param['intent_city'],
                'ExhibitOn': param['exhibit_on'],
                'RequireArea': param['require_area'],
                'IntentExhibition': param['intent_exhibit'],
                'X-Requested-With': 'XMLHttpRequest'
            }
        else:
            data = {
                'ID': param['id'],
                'ServiceItem': param['service_item'],
                'ExhibitionName': param['exhibition_name'],
                'BoothArea': param['area'],
                'FinishOn': param['finish_on'],
                'Budget': param['budget'],
                'Enterprise': param['company_name'],
                'X-Requested-With': 'XMLHttpRequest'
            }
        web_response = requests.post(param['url'], data=data)
        res = json.loads(web_response.text)['success']
        assert res == True

