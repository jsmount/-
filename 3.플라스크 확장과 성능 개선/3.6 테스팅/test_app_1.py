import unittest
from my_app import app # my_app 모듈에서 플라스크 애플리케이션을 가져옵니다.

# BasicTestCase 클래스는 unittest.TestCase를 상속받습니다.
class BasicTestCase(unittest.TestCase):

    # index 라우트를 테스트하는 메서드입니다.
    def test_index(self):
        # 플라스크 애플리케이션을 위한 테스트 클라이언트 인스턴스를 생성합니다.
        tester = app.test_client(self)
        # 테스트 클라이언트를 사용하여 루트 URL로 GET 요청을 보냅니다.
        response = tester.get('/', content_type='html/text')
        # 응답받은 상태 코드가 200인지 확인합니다.
        self.assertEqual(response.status_code, 200)