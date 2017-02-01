#DB Forum-a buggy web forum server backed by a good database
#The forumdb module is where the database interface code goes

import forumdb

#Other modules used to run a web server
import cgi
from wsgiref.simple_server import make_server
from wsgiref import util

#HTML template for the forum page

HTML_WRAP= """ \
<!DOCTYPE html>
<html>
    <head>
        <title>DB Forum</title>
        <style>
        h1,form {text-align: center;}
        textarea {width:400px; height: 100px;}
        div.post {border: 1px solid #999;
                padding: 10px 10px;
                margin: 10px 20%%;}
        hr.postbound {width: 50%%;}
        em.date {color: #999;}
        </style>
    </head>

    <body>

    </body>
</html>
"""

#get posts from database
posts = forumdb.GetAllPosts()

#send results
headers= [('Content-type', 'text/html')]
resp('200 OK', headers)
return [HTML_WRAP % ''.join(POST % p for p in posts)]

##Request handler for posting - inserts to database

def Post (env, resp):
    
