import requests
import unittest

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

text = 'hello'
params = {'key': API_KEY, 'text': text, 'lang': 'en-ru'}
response = requests.get(URL, params=params)
# print(response)
json_ = response.json()
# print(json_)

def answer_200():
    return json_['code']

def translate_result():
    return json_['text']

def language_from_to():
    return json_['lang']


class TestSum(unittest.TestCase):

    def test_answer_200(self):
        self.assertEqual(answer_200(), 200)
        print('Код ответа соответствует 200')

    def test_translate_result(self):
        self.assertEqual(translate_result(), ['привет'])
        print('результат перевода правильный - "привет"')

    def test_language_from_to(self):
        self.assertEqual(language_from_to(), 'en-ru', 'Should be "en-ru"')


if __name__ == '__main__':
    unittest.main()
