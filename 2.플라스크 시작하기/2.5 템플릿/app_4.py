# 탬플릿 상속
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/about')
def about_page():
    # 'render_template' 함수를 사용하여 'about.html' 템플릿을 랜더링합니다.
    # 플라스크는 'about.html'과 함께 이 템플릿이 상속하는 모든 부모 템플릿('base.html')을 랜더링하여 최종 HTML을 생성합니다.
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=False)