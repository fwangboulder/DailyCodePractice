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
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                output = ""
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
                    output += "</br></br></br>"

                output += "</body></html>"

                # send the message back to the client
                self.wfile.write(output)
                # print output
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


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
