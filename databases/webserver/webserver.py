# use BaseHTTPServer as a basis for building functioning Web servers.
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# decipher the message taht was sent from the server.
import cgi

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
            if self.path.endswith("/hello"):
                # look for path and server sends 200 indicating sucessfull
                # get request
                self.send_response(200)

                # use send_header function to indicate replying with text/html
                self.send_header('Content-type', 'text/html')
                # send a blank line indicating the end of HTTP headers
                self.end_headers()
                # create the response
                message = ""
                message += "<html><body>Hello!<a href='/Bye'>"
                message += '''<form method='POST' enctype='multipart/form-data'
                action='/hello'><h2>What would you like me to say?</h2>
                <input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                message += "</body></html>"

                # send the message back to the client
                self.wfile.write(message)
                print message
                return
            if self.path.endswith("/Bye"):
                # look for path and server sends 200 indicating sucessfull
                # get request
                self.send_response(200)

                # use send_header function to indicate replying with text/html
                self.send_header('Content-type', 'text/html')
                # send a blank line indicating the end of HTTP headers
                self.end_headers()
                # create the response
                message = ""
                message += "<html><body>Bye! <a href='/hello'>Back to Hello"
                message += '''<form method='POST' enctype='multipart/form-data'
                action='/hello'><h2>What would you like me to say?</h2>
                <input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                message += "</body></html>"

                # send the message back to the client
                self.wfile.write(message)
                print message
                return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        # Post requests from a browser require data to be submitted, like with a form.
        # Overide the method in the base http request handler superclass

        try:
            # send response code indicating a successfull Post
            self.send_response(301)
            self.end_headers()

            # cgi.parse_header function parses a HTML form header into
            # a main value and dictionary of parameters.
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))

            # check to see if this form data being received.
            if ctype == 'multipart/form-data':
                # if so, use cgi_multipart function to collect all fields in a
                # form.
                fields = cgi.parse_multipart(self.rfile, pdict)

                # get out the value of a specific fields or sets of fields.
                # store them in an array.

                # call the field message  and when create HTML form.
                messagecontent = fields.get('message')

                # received a post request
                message = ""
                message += "<html><body>"
                message += " <h2>Ok, how about this: </h2>"
                message += " <h1> %s </h1>" % messagecontent[0]

                message += '''<form method='POST' enctype='multipart/form-data'
                action='/hello'><h2>What would you like me to say?</h2>
                <input name="message" type="text" ><input type="submit" value="Submit"> </form>'''

                message += "</body></html>"

                self.wfile.write(message)
                print message  # print out for debugging.
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
