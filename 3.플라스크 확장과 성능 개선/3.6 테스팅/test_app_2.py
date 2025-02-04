import unittest
from my_app import app

class AdvancedTestCase(unittest.TestCase):

    def setUp(self):
        # 플라스크 애플리케이션의 테스트 클라이언트를 생성합니다.
        # self.tester는 테스트 동안 사용할 가상의 클라이언트 객체입니다.
        self.tester = app.test_client(self)

    def tearDown(self):
        # 테스트가 끝난 후 정리 작업을 수행합니다. 현재는 비어 있는 상태입니다.
        pass

    def test_index(self):
        # self.tester 객체를 사용하여 루트 URL('/')로 HTTP GET 요청을 보냅니다.
        response = self.tester.get('/', content_type='html/text')
        # 응답의 상태 코드가 200인지 확인합니다.
        self.assertEqual(response.status_code, 200)