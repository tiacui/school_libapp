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
    - Refer to:
    ```
    "form"
    https://www.w3schools.com/html/html_forms.asp
    
    
    "action" attribute of "Form":
    https://www.w3schools.com/html/html_forms_attributes.asp
    
    - use "https://example.com/login" for now (as a place holder)
    
    
    "input" and "label" Element
    https://www.w3schools.com/html/html_form_input_types.asp
    https://www.w3schools.com/html/html_form_input_types.asp
    ```

==============================

Task 2: using CSS to make the "logins.html" interface looks better.

- 1), using "inline CSS" to change the font color of Menu "home" to Green
- 2), using the following code as "internal CSS" to make the page look better. make sure all the selectors are applied.

```
 body {
            margin: 0;
            font-family: Arial;
        }
        
        /* styling for Menu bar */
        .menu {
            background: #333;
            color: white;
            padding: 10px;
        }
        
        /* styling for "Login" div */
        .login {
            border: 1px solid #ccc;
            padding: 20px;
            margin: 50px auto;
            width: 300px;
        }
        
        /* styling for Footer */
        .footer {
            background: #eee;
            padding: 10px;
            text-align: center;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
        
        /* styling for form "input" */
        input {
            display: block;
            margin: 10px 0;
            padding: 5px;
            width: 100%;
        }

        /* styling for "login" button */
        #login_button {
            padding: 8px 15px;
            background: #333;
            color: white;
            border: none;
        }

```

Refer to ```https://www.w3schools.com/html/html_css.asp, https://www.w3schools.com/cssref/css_selectors.php```
