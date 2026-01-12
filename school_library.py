import json
import pprint
import random

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

    def list_books(self):
        print("listing books")
        print("book_id     author    name     stocks")
        for book in self.books:

            print(book['book_id'], "    ",book['author'], "    ", book['name'], "    ", book['stock'])
            print()

    
    def add_book(self):
        print("adding books")
        book_id = random.randint(100000,999999)
        name = input("name: ")
        author = input("author:")
        stock = input("stock: ")
        
        new_book = {"book_id": book_id, "name": name, "author": author, "stock": int(stock)}

        self.books.append(new_book)
        self.save_data()


    
    def borrow_book(self, book_id):
        print("borrow " + book_id)
        for book in self.books:
            if book["book_id"] == int(book_id):
                book["stock"] = book["stock"] - 1
                print("book borrowed successfully")
                self.save_data()

     def return_book(self, book_id):
        print("returned " + book_id)
        for book in self.books:
            if book["book_id"] == int(book_id):
                book["stock"] = book["stock"] + 1
                print("book returned successfully")
                self.save_data()


    
    

def main():
    car_library = SchoolLibrary("caringbah")
    car_library.load_data()
    print("my library is", car_library.name)
    print(pprint.pprint(car_library.books))
    car_library.borrow_book(input('book_id: '))

    #library.books[0]['name'] = "hello"
    #library.save_data()



if __name__ == '__main__':
    main()