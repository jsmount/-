# 플라스크에서의 요청 처리
from flask import Flask, request

app = Flask(__name__)

@app.route('/query')
def query_example():
    language = request.args.get('language')
    return f"Requested language: {language}"

# http://127.0.0.1:5000/query?language=python으로 접속
# language=python 부분이 쿼리 매개변수
# 쿼리 매개변수: ? 이후에 나오는 키-값 쌍의 데이터로 웹 서버에 추가 정보를 제공하기 위해 사용
if __name__ == "__main__":
    app.run(debug=False)