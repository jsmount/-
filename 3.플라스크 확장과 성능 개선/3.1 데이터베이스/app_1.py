from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 데이터베이스 연결 URI 설정정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name' # 유저 이름, 비번 알맞게 입력하기기

# SQLAlchemy 인스턴스 초기화
db = SQLAlchemy(app)

# 데이터베이스 모델 정의
class User(db.Model):
    # 테이블 이름 직접 지정 (이 부분을 생략하면 기본적으로 클래스 이름을 소문자화한 'user'가 됩니다.)
    __tablename__ = 'users'
    # 각 필드 정의
    id = db.Column(db.Integer, primary_key=True) # 사용자 ID 기본 키로 설정
    username = db.Column(db.String(80), unique=True, nullable=False) # 사용자 이름, 중복 불가능 및 필수
    email = db.Column(db.String(120), unique=True, nullable=False) # 이메일 주소, 중복 불가능 및 필수

    def __repr__(self):
        return '<User %r>' % self.username # 객체를 문자열로 표현할 때 사용할 형식
    
# 애플리케이션 컨텍스트 안에서 DB 테이블을 생성합니다.
with app.app_context():
    # 모델에 정의된 모든 테이블을 데이터베이스에 생성합니다.
    db.create_all()

# 라우트 정의
@app.route('/')
def index():
    # 데이터 생성(Create)
    new_user = User(username='john', email='john@example.com')
    db.session.add(new_user)
    db.session.commit()

    # 데이터 조회(Read)
    user = User.query.filter_by(username='john').first()

    # 데이터 업데이트(Update)
    user.email = 'john@newexample.com'
    db.session.commit()

    # 데이터 삭제(Delete)
    db.session.delete(user)
    db.session.commit()

    return 'CRUD operations completed'

if __name__ == '__main__':
    app.run(debug=False)