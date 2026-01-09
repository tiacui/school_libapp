import datetime







def log(name, result):
    with open("log/log.txt", "a") as logfile:
        cur_time = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')
        logfile.write(cur_time + " " + name + " " + result + "\n")




def userlogin():
    file = "config/credentials.txt"
    
    while True:
        username = input("enter username: ")
        password = input("enter your password: ")

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