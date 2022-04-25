import requests
import unittest


class YandexTranslateTest(unittest.TestCase):

    def test_smoke(self):
        response = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params={
            'key': 'trnsl.1.1.20200403T072622Z.1505b0f5f82fe645.8cc2ea18da93c3209773dc80aa5cdd1e03b60cc4',
            'text': 'Hello World',
            'lang': 'en-ru'
        })
        self.assertEqual(response.status_code, 200)

        data = response.json()['text'][0]
        self.assertEqual(data, 'Привет Мир')



