import json
import pprint
import random
import datetime


def log(name, message):
    with open("log/log.txt", "a") as logfile:
        cur_time = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')
        logfile.write(cur_time + " " + name + " " + message + "\n")


def user_login():
    file = "config/credentials.txt"
    
    while True:
        username = input("username: ")
        password = input("password: ")

        with open(file, "r") as filedata:
            for line in filedata.readlines():
                line = line.strip()

                user_and_password = line.split(":")

                username123 = user_and_password[0]
                password123 = user_and_password[1]

                if username == username123 and password == password123:
                    print("login successful")
                    log(username, "success")
                    return username
        log(username, "fail")


class SchoolLibrary:
    def __init__(self, name,):
        self.name = name
        self.books = None


    def load_data(self):
        with open("books/books.json", "r") as loaddata:
            self.books = json.load(loaddata)
            print("data loaded")


    def save_data(self):
        with open("books/books.json", "w") as loaddata:
            json.dump(self.books, loaddata)
            print("data saved")

    def list_books(self, username):
        print("listing books")
        print("book_id     author     name      stocks")
        log(username, "is listing books")
        for book in self.books:

            print(book['book_id'], "    ",book['author'], "    ", book['name'], "    ", book['stock'])
            print()

    
    def add_book(self, username):
        print("adding books")
        book_id = random.randint(100000,999999)
        name = input("name: ")
        author = input("author:")
        stock = input("stock: ")
        
        new_book = {"book_id": book_id, "name": name, "author": author, "stock": int(stock)}
        log(username, "book added")

        self.books.append(new_book)
        self.save_data()


    
    def borrow_book(self, book_id, username):
        print("borrow " + book_id)
        for book in self.books:
            if book["book_id"] == int(book_id):
                book["stock"] = book["stock"] - 1
                print("book borrowed successfully")
                log(username, "book borrowed")
                self.save_data()

    def return_book(self, book_id, username):
        print("returned " + book_id)
        for book in self.books:
            if book["book_id"] == int(book_id):
                book["stock"] = book["stock"] + 1
                print("book returned successfully")
                log(username, "book returned")
                self.save_data()