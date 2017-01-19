### Helpful Tips####
## Always automatically escape variables when possible
## minimize code in templates
##minimize html in the code

####Templates###
# seperate different types of code
# make more readable code
# more secure websites
# html that is easier to modify


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

app=webapp2.WSGIApplication([('/',MainPage),('/fizzbuzz',FizzBuzzHandler)], debug=True)
