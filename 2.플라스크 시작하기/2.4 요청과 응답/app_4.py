# make_response() 함수는 headers를 직접 인자로 전달하는 것도 가능하고, 생성된 응답 객체에 나중에 추가도 가능

from flask import Flask, make_response

app = Flask(__name__)

# 생성 시점에 모든 정보를 한 번에 넘길 때 좋음음
@app.route('/direct')
def direct_response():
    headers = {'X-Example': 'DirectHeader'}
    return make_response("Direct Response", 200, headers)

# 응답 객체를 조금 더 유동적으로 다룰 필요가 있을 때 좋음
@app.route('/custom')
def custom_response():
    response = make_response("Custom Response", 202)
    response.headers['X-Examlpe'] = 'CustomHeader'
    return response

if __name__ == '__main__':
    app.run(debug=False)