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

In step 3, use a fake restaurant and menu first.

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}

**Authetication and authorization**

 project5.py

Add some security to the applicaiton and publish it on the internet.
Use Google+ and Facebook Sign_in

Knowledge required:
Python, Flask web development framework, JavaScript,
using JQuery to make Ajax calls

      **How to run it?**

      1. Go to templates folder. type in your correct client ID in login.html file
      (How to get it? read AutheticationAuthorization/README.md)

      2. Download ClientID JSON file and rename it as client_secrets.json, store
      it in flask folder, same as project5.py.

      3. $python project5.py

      4. http://localhost:9000/login

      5. If you see an error about JSON serializable. update your versions of Flask.

        ```
        $pip install werkzeug==0.8.3

        $pip install flask==0.9

        $pip install Flask-Login==0.1.3

        Note: If you get a permissions error, you will need to include sudo at the beginning of each command. That should look like this: sudo pip install flask==0.9

        ```
