Goal: create a web interface (front end) for the library app.

Task 1: create a simple html page for the login interface, which will have:
- menu bar
- school logo
- login form
- footer

=======================

- under ```school_libapp```, create a folder ```templates``` (where html files will be stored)
- under ```templates```, create a file ```login.html``` (i.e. ```templates/login.html```) which will be the login page
- Edit ```login.html``` to create a HTML skeleton, refer to ```https://www.w3schools.com/html/html_head.asp```
- in ```login.html```, create 3 ```<div>``` elements, each for: "menu bar", "login form", "footer" sections. refer to ```https://www.w3schools.com/html/html_div.asp```
- in the ```<div>``` for menu, create 3 links (using ```<a>``` tag, all point to ```https://example.com/``` for now). refer to ```https://www.w3schools.com/html/html_links.asp```:
  - ```Home```
  - ```About```
  - ```Contact```
- in the ```<div>``` for footer (last one), enter ```Copyright 2023 Caringbah High School Library```
- in the ```<div>``` for login form:
  - create a ```<img>``` tag which point to ```https://assets.schools.nsw.gov.au/content/dam/doe/sws/schools/c/caringbah-h/logo.png```, so we will have a logo on the page. (refer to ```https://www.w3schools.com/html/html_images.asp```)
  - create a ```<h2>``` tag with text ```Login```, refer to 
  - create a ```<form>``` which points to ```https://example.com/login``` with the following:
    - username input field
    - password input field
    - "login" button
