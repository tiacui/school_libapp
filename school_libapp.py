import sys
import datetime
import json








def log(name, result):
    with open("log/log.txt", "a") as logfile:
        cur_time = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')
        logfile.write(cur_time + " " + name + " " + result + "\n")




def userlogin():
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
        log(username, "fail1")

    
    
              


user = userlogin()
print("you are: ", user)

if user == "admin":
    print("\n\n***********************************")
    print("* 1) list all books")
    print("* 2) add books")
    print("* 3) remove books")
    print("* q) quit")
    print("***********************************")

    select = input("please select a number 1-3: ")
    if select == "1":
        print("listing all books here")
    elif select == "2":
        print("add books here")
    elif select == "3":
        print("remove books here")
    elif select == "q":
        print("quit...")
        sys.exit()
    else:
        print("invalid number")
elif user == "student1" or "student2":
    print("***********************************")
    print("* 1) list all books")
    print("* 2) borrow a book")
    print("* 3) return a book")
    print("***********************************")

    select = input("select a number 1-3:")
    if select == "1":
        print("listing all books here")
    elif select == "2":
        print("borrowing books here")
    elif select == "3":
        print("returning books here")
    else:
        print("invalid number")