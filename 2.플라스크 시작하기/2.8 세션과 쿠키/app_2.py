from flask import Flask, make_response, request, abort

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    resp = make_response('쿠키를 설정합니다.')
    resp.set_cookie('username', 'John')
    return resp

@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username', '게스트')
    return f'쿠키로부터 얻은 사용자 이름: {username}'

# 쿠키가 설정된 사용자만 접근 가능한 라우트
@app.route('/secret')
def secret():
    username = request.cookies.get('username')
    if not username:
        # 쿠키가 없다면 접근 금지 메시지 반환
        abort(403, description='접근 권한이 없습니다. 먼저 쿠키를 설정해주세요.')
    return f'환영합니다, {username}님! 비밀 페이지에 접속하셨습니다.'

@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('쿠키를 삭제합니다.')
    resp.delete_cookie('username')
    return resp

if __name__ == '__main__':
    app.run(debug=False)