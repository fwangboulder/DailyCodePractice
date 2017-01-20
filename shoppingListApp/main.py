### Helpful Tips####
## Always automatically escape variables when possible
## minimize code in templates
##minimize html in the code

####Templates###
# seperate different types of code
# make more readable code
# more secure websites
# html that is easier to modify
#########
#for signup HW2##
import re
from string import letters


import os
import webapp2

#shopping list probelms if no templates: a pain to change, no synax highlighting,
#ugly code and error prone

#add template
import jinja2

#initializes jinja2
# escape html use autoescape
# use | safe to remove escape for cases
#ex: in shopping_list.html file, try {{item | safe}} and add <h1>Eggs</h1>
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape=True)



#move this part to /templates/shopping_list.html
#form_html="""
#<form>
#<h2>Add a Food</h2>
#<input type="text" name='food'>
#%s
#<button>Add</button>
#</form>
#"""
# hidden_html="""
# <input type="hidden" name="food" value="%s">
# """
# item_html="""<li>%s</li>"""
# shopping_list_html="""
# <br>
# <br>
# <h2>Shopping List</h2>
# <ul>
# %s
# </ul>
#
# """
class Handler(webapp2.RequestHandler):
    def write(self,*a, **kw):
        self.response.out.write(*a,**kw)

    #add two functions for template-lesson
    def render_str(self,template, **params):
        t=jinja_env.get_template(template)
        return t.render(params)
    def render(self,template,**kw):
        self.write(self.render_str(template,**kw))

class MainPage(Handler):
    def get(self):
        # n=self.request.get('n')
        # if n.isdigit():
        #     n=int(n)
        items=self.request.get_all("food")
        self.render("shopping_list.html",items=items)

        # output=form_html
        # output_hidden=""
        # output_shopping=""
        #
        #
        # if items:
        #     output_items=""
        #     for item in items:
        #         output_hidden+=hidden_html % item
        #         output_items+=item_html % item
        #     output_shopping+=shopping_list_html % output_items
        #     output+=output_shopping
        # output=output % output_hidden
        # self.write(output)
class  FizzBuzzHandler(Handler):
        def get(self):
            n=self.request.get('n',0)
            n=n and int(n)
            self.render('fizzbuzz.html',n=n)
#check localhost:8080/rot13 to see the ROT13
class Rot13(Handler):
    def get(self):
        self.render("ROT13.html")
    def post(self):
        rot13=""
        text=self.request.get('text')
        if text:
            rot13=text.encode('rot13')
        self.render('ROT13.html',text=rot13)

#######################################
#for Homework 2 signup
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class Signup(Handler):

    def get(self):
        self.render("signup.html")

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username = username,
                      email = email)

        if not valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.render('signup.html', **params)
        else:
            self.redirect('/welcome?username=' + username)

class Welcome(Handler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            self.render('welcome.html', username = username)
        else:
            self.redirect('/signup')


#######################################



app=webapp2.WSGIApplication([('/',MainPage),('/fizzbuzz',FizzBuzzHandler),('/rot13',Rot13),('/signup',Signup),('/welcome',Welcome)], debug=True)
