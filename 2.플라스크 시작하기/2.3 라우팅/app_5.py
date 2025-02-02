from flask import Flask

app = Flask(__name__)

@app.route('/int/<int:var>')
def int_type(var: int):
    return f'Integer: {var}'

@app.route('/float/<float:var>')
def float_type(var: float):
    return f'Float: {var}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath: {subpath}'

@app.route('/uuid/<uuid:some_id>')
def show_uuid(some_id):
    return f'UUID: {some_id}'

if __name__ == '__main__':
    app.run(debug=False)