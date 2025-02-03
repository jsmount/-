# 매크로
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/messages')
def show_messages():
    return render_template("messages.html")

if __name__ == '__main__':
    app.run(debug=False)