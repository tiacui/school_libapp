# school_libapp
learning Python


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
