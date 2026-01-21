from flask import Flask, request

app = Flask(__name__)

@app.route("/login")
def user_login():
    username = request.args.get('username')
    password = request.args.get('password')
    return username + " " + password

if __name__ == '__main__':
    app.run(debug=True, port=5000)