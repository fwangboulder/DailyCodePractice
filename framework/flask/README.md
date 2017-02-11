Udacity Full Stack Web Developer nanadegree

Course: Full Stack Foundations.

Working with CRUD

Making a Web server

Developing with Framework

Iterative development


This is the part of Developing with Framework. Most popular frameworks: RubyonRails.net, Django

Six steps:

Step I Basic compoments of an app using framework

Step II Connect to database via SQL Alchemy to view all of the items.

Step III Use templates to write HTML code

Step IV Build the URLs using Flask functions: url_for

Step V Create forms and use message flashing to notify the user.

Step VI Use flash to send JSON message

Step VII Style the app using CSS

Before you run project*.py,
run lotsofmenu.py first to generate restaurant databases once.

$python lotsofmenu.py

Create a menu app: Flask framework.

**project0.py**

A minimum Flask app: Flask Hello World Web app

**project.py**

Add code of sqlalchemy and database engine in sessionmaker

Run:

```
$python project.py

http://localhost:9000/

http://localhost:9000/hello

```

**project1.py**

```
$python project1.py

http://localhost:9000/restaurants/1/

http://localhost:9000/restaurants/1/new/

http://localhost:9000/restaurants/1/1/edit/

http://localhost:9000/restaurants/1/1/delete/

```

**project2.py**

apply templates and url_for function

Create a folder called templates.

```
$python project2.py

http://localhost:9000/restaurants/1/menu

http://localhost:9000/restaurants/1/new

http://localhost:9000/restaurants/1/1/edit

http://localhost:9000/restaurants/1/5/delete

```

**project3.py**

add fashing message: flashing works in Flask but uses a concept of sessions.
sessions are a way web server can store information across multiple web pages.

from flask import flash

```
$python project3.py

http://localhost:9000/restaurants/1/menu

```
test flash message by add new item, edit item and delete item.

**Styling**

Create a folder called static.
add styles.css file. Modify all  files in templates.

**project4.py**

Responding with JSON

Add  serialize function to be able to send JSON objects in a
serializable format in data_setup.py


from flask import jsonify
Making an API Endpoint (make request)
add function restaurantMenuJSON(restaurant_id)
Run:

```
$python project4.py

http://localhost:9000/restaurants/1/menu/JSON

```

Add a JSON Method to get one specific menu item
function: menuItemJSON(restaurant_id, menu_id)

```
http://localhost:9000/restaurants/1/menu/1/JSON

```


###########################################

**Iterative Development**

Checklist:
1. Mock-ups
2. Add Routes
3. Add templates and forms
4. CRUD functionality
5. API endpoints
6. styling app and flash message.
