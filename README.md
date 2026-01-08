# school_libapp
learning Python

git commands
=================================
1, each day, before starting to work on the code, under ```C:\Users\xinyo\library_project```:
- run command ```git pull``` to sync the remote files from ```https://github.com/tiacui/school_libapp```

2, each day, when finishing the work, under ```C:\Users\xinyo\library_project```, run the commands:
- ```git add .``` to add all changes
- ```git commit -m "xxx"``` to commit the updates
- ```git push``` to push the code to the remote repo, ```https://github.com/tiacui/school_libapp```


Library Book Management System
=================================

Goal: 

Create a simple library book management system, which can:
- have users like admins, students
- ......



=================================

Task 1:

- create a folder ```library_project``` under home directory ```C:\Users\xinyo\```, for example, ```C:\Users\xinyo\library_project```			[comment: all future work will be saved here]

- under "library_project", create a python script like ```school_libapp.py```								[comment: this will be the main program library admins and students use]

- in "school_lib_app.py", create the scripts in the following structure:
```
def main():
    ...

if __name__ == '__main__':
    main()
```

- under the ```main()``` function, achieve the following:
    - 1), prompt for username.
    - 2), if the username entered is "admin", print "Hello admin, you are logged in as admin" and exit. if the username entered is "student1" or "student2", print "Hello [name], you are logged in as a student" and exit.
    - 3), if the username is not in #1) and #2), print "sorry, wrong username entered" and prompt for username.

=================================

Task 2: the app should read username/password from file ```config\credentials.txt```

- create a folder ```config``` under ```C:\Users\xinyo\library_project```, i.e.```C:\Users\xinyo\library_project\config```                     [comment: configuration files will be saved here]
- create the file ```config\credentials.txt```, with the following content (i.e. username and password are seperated by ":"):
  ```
  admin:admin123
  student1:student111
  student2:student222
  ```
- modify the ```student_login()``` function, to make it:
  - also prompt for "password" besides "username"
  - open the file ```config\credentials.txt```, read each line of it, use function ```split()``` to split with ```:```, so you obtain the username and corresponding password in a line in ```config\credentials.txt```
  - if the username/password matches the username/password a user provided, authentication is successful, continue to the section "Hello ***, you are logged in as ***"
  - if the username/password a user provided failed to match any of the lines in ```config\credentials.txt```, authentication fails, and prompt the user to login again.

Key points:
- read lines from a file
  - can use ```with open(filename, 'r') as f:```;
  - or can use ```f = open(filename, 'r'); ...; f.close()```
  - functions like ```readlines()``` can be used to read from files
  - new line characters like ```\n``` needs to be striped 

 =================================

 Task 3: write login (successful, failed) events to logs

 - create a folder ```logs``` under ```C:\Users\xinyo\library_project```, i.e.```C:\Users\xinyo\library_project\logs```                     [comment: log files will be saved here]
 - create a new function like ```write_logins()``` to do the following:
   - 2026-01-08T12:01:01Z username success|failed
 - update the ```student_login()```, to make it call ```write_logins()``` to write an event to the log files everytime a login is attempted

 Key points:
 - writing lines to a file
 - timestamps, UTC and timezone


