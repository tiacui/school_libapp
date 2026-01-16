import sys
import school_library


def main():

    user = school_library.user_login()
    print("you are: ", user)
    car_library = school_library.SchoolLibrary("caringbah")
    car_library.load_data()


    while True:
        if user == "admin":
            print("\n\n***********************************")
            print("* 1) list all books")
            print("* 2) add books")
            print("* 3) view logs")
            print("* q) quit")

            print("***********************************")

            select = input("please select a number 1-3: ")
            if select == "1":
                print("listing all books here")
                car_library.list_books(user)
                
            elif select == "2":
                print("add books here")
                car_library.add_book(user)
              
            elif select == "q":
                print("quit...")
            
            elif select =="3":
                print("logs: ")
                car_library.view_logs()
              
                sys.exit()
            else:
                print("invalid number")
        elif user == "student1" or user == "student2":
            print("***********************************")
            print("* 1) list all books")
            print("* 2) borrow a book")
            print("* 3) return a book")
            print("* q) quit")
            print("***********************************")

            select = input("select a number 1-3:")
            if select == "1":
                print("listing all books here")
                car_library.list_books(user)
            elif select == "2":
                print("borrowing books here")
                car_library.borrow_book(input('book_id: '))
            elif select == "3":
                print("returning books here")
                car_library.return_book(input('book_id: '))
            elif select == "q":
                print("quit...")
                sys.exit()
            
            else:
                print("invalid number")


if __name__ == '__main__':
    main()