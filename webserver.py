from flask import Flask, request, render_template
from school_library import user_login, SchoolLibrary

app = Flask(__name__)
lib = SchoolLibrary("My Library")
lib.load_data()

@app.route("/login")
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    user = user_login(username=username, password=password)
    if user:
        books_data = lib.list_books(user, format="aaa")
        return render_template("books.html", books_list=books_data)
    else:
        return "failed" 

if __name__ == '__main__':
    app.run(debug=True, port=5000)