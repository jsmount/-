# 상태 코드와 헤더 설정
# 주용 상태 코드
# 200 OK -> 요청이 성공적으로 처리 됨, 201 Created -> 요청이 성공적으로 처리되어 새 리소스가 생성됨
# 400 Bad Request -> 서버가 요청을 이해하지 못함, 401 Unauthorized -> 인증이 필요한 페이지를 요청함
# 403 Forbidden -> 서버가 요청을 거부함, 404 Not Found -> 요청한 리소스를 찾을 수 없음
# 500 Internal Server Error -> 서버 내부 에러가 발생함

from flask import Flask, make_response
# make_respons() 함수를 사용해서 상태 코드와 헤더를 지정하는 핼퍼 함수를 제공함

app = Flask(__name__)

@app.route('/response')
def response_example():
    # 응답 객체를 생성합니다. "Hello with header"는 응답 바디이며, 200은 HTTP 상태 코드입니다.
    resp = make_response("Hello with header", 200)
    # 'Custom-Header'라는 이름의 사용자 정의 헤더를 설정하고 'custom-value' 값을 지정합니다.
    resp.headers['Custom-Header'] = 'custom-value'
    # 설정한 헤더와 함께 응답 객체를 반환합니다.
    return resp

if __name__ == '__main__':
    app.run(debug=False)