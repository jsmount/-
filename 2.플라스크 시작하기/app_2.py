from flask import Flask, url_for

app = Flask(__name__)

# 기본 홈페이지 경로
# @app.route('/')
# def index():
#     return '홈페이지에 오신 것을 환영합니다!'

# 홈페이지 경로를 /home으로 변경
@app.route('/home')
def index():
    return '홈페이지에 오신 것을 환영합니다!'

# 사용자 정보 페이지 경로
@app.route('/user/<username>')
def profile(username):
    # url_for()를 사용하여 'index' 뷰 함수의 URL을 생성합니다.
    return f'{username}님의 프로필 페이지입니다. 홈으로 가기: {url_for("index")}'


if __name__ == "__main__":
    app.run(debug=False)