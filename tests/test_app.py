from unittest import TestCase
from app import ipca_app


class Test(TestCase):
    def setUp(self):
        app = ipca_app.test_client()
        self.response = app.get('/')

    # Testamos se a resposta e 200 ("ok")
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    # Testamos se a nossa home retorna uma string quando url vazia
    def test_empty_response(self):
        self.assertEqual("Empty fields <br> Use example: /?money_value=20&year=1997",
                         self.response.data.decode('utf-8'))

    # Testamos se o content_type da resposta da home esta correto
    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)
