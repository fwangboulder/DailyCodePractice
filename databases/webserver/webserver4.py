
# List out all Restaurant Name.
# add Edit and Delete link (doing nothing at the moment) to each restaurant and add a new page for create
# new restaurant.
# add edit link ( able to edit) and a new edit URL
# add delete link (able to delete ) and a new delete URL

# use BaseHTTPServer as a basis for building functioning Web servers.
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# decipher the message taht was sent from the server.
import cgi

# import CRUD Operations
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# web server code has two main sections: main method and the handler class

# Handler code indicates what code to execute based on the type of
# HTTP request that is sent to the server.


class WebServerHandler(BaseHTTPRequestHandler):

    # do_Get function handles all get requests web server recieves.
    # View infromation already on the server; Visit the URLs.

    def do_GET(self):
        # figure out which rescource to access ,simple matching the ending of
        # URL path
        try:

            #  Create /restarants/new page
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"
                output += "<input name = 'newRestaurantName' type = 'text' placeholder = 'New Restaurant Name' > "
                output += "<input type='submit' value='Create'>"
                output += "</br></br></br><a href = '/restaurants' > Back to Restaurants</a></br></br>"
                output += "</form></body></html>"
                self.wfile.write(output)
                return
            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(
                    id=restaurantIDPath).one()
                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>"
                    output += myRestaurantQuery.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action = '/restaurants/%s/edit' >" % restaurantIDPath
                    output += "<input name = 'newRestaurantName' type='text' placeholder = '%s' >" % myRestaurantQuery.name
                    output += "<input type = 'submit' value = 'Rename'>"
                    output += "</br></br></br><a href = '/restaurants' > Back to Restaurants</a></br></br>"
                    output += "</form></body></html>"
                    self.wfile.write(output)
                    return
            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]

                myRestaurantQuery = session.query(Restaurant).filter_by(
                    id=restaurantIDPath).one()
                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>Are you sure you want to delete %s?" % myRestaurantQuery.name
                    output += "<form method='POST' enctype = 'multipart/form-data' action = '/restaurants/%s/delete'>" % restaurantIDPath
                    output += "<input type = 'submit' value = 'Delete'>"
                    output += "</br></br></br><a href = '/restaurants' > Back to Restaurants</a></br></br>"
                    output += "</form></body></html>"
                    self.wfile.write(output)
                    return

            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                output = ""
                # Create a Link to create a new menu item
                output += "<a href = '/restaurants/new' > Make a New Restaurant Here </a></br></br>"
                # look for path and server sends 200 indicating sucessfull
                # get request
                self.send_response(200)

                # use send_header function to indicate replying with text/html
                self.send_header('Content-type', 'text/html')
                # send a blank line indicating the end of HTTP headers
                self.end_headers()
                # create the response

                output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"
                    # -- Add Edit and Delete Links
                    output += "<a href ='/restaurants/%s/edit' >Edit </a> " % restaurant.id
                    output += "</br>"
                    output += "<a href ='/restaurants/%s/delete'> Delete </a>" % restaurant.id
                    output += "</br></br></br>"

                output += "</body></html>"

                # send the message back to the client
                self.wfile.write(output)
                # print output
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

# Make POST method
    def do_POST(self):
        try:
            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(
                    id=restaurantIDPath).one()
                if myRestaurantQuery:
                    session.delete(myRestaurantQuery)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    restaurantIDPath = self.path.split("/")[2]

                    myRestaurantQuery = session.query(Restaurant).filter_by(
                        id=restaurantIDPath).one()
                    if myRestaurantQuery != []:
                        myRestaurantQuery.name = messagecontent[0]
                        session.add(myRestaurantQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                    # Create new Restaurant Object
                    newRestaurant = Restaurant(name=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        except:
            pass
# Instantiate the server and specify what port it will listen on.


def main():
    try:
        port = 9000
        server = HTTPServer(('', port), WebServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."

        # stop the server
        server.socket.close()

if __name__ == '__main__':
    main()
