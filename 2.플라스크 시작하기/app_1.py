from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {username}"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Logging in..."   
    else:
        return "Login Form"
    
if __name__=="__main__":
    app.run(debug=False)