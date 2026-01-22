from flask import Flask, request
from school_library import user_login
app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    user = user_login(username=username, password=password)
    if user:
        return "success"
    else:
        return "failed"

if __name__ == '__main__':
    app.run(debug=True, port=5000)