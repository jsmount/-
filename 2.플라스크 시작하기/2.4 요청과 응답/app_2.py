# 플라스크에서의 응답 처리

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/json')
def json_example():
    # jsonify를 사용하여 JSON 형식의 응답을 반환합니다.
    return jsonify({"message": "Hello, World"})

if __name__ == '__main__':
    app.run(debug=False)