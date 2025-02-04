import unittest
from my_app import app

class AdvancedTestCase(unittest.TestCase):

    # setUp 메서드는 각 테스트 메서드를 실행하기 전에 호출됩니다.
    def setUp(self):
        # self.tester는 플라스크의 test_client 인스턴스를 참조합니다.
        # 이를 통해 실제 HTTP 서버를 구동하지 않고도 HTTP 요청을 테스트할 수 있습니다.
        self.tester = app.test_client(self)

    # test_index 메서드는 루트 경로('/')에 대한 테스트를 정의합니다.
    def test_index(self):
        # 루트 경로에 GET 요청을 보냅니다. content_type은 요청의 타입을 지정합니다.
        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # test_index_test 메서드는 루트 경로의 응답 텍스트를 테스트합니다.
    def test_index_test(self):
        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.data, b'Hello, World!')

    # test_another_route 메서드는 다른 경로('/another')에 대한 테스트를 정의합니다.
    def test_another_route(self):
        response = self.tester.get('/another', content_type='html/text')
        # 해당 경로가 존재하지 않으므로 상태 코드가 404인지 확인합니다.
        self.assertEqual(response.status_code, 404)