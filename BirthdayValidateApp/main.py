#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
m={'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'}
def valid_month(user_month):
    if user_month.isdigit() and 1<=int(user_month)<=12:
        return True
    user_month=user_month.lower()
    user_month=user_month.capitalize()
    if user_month in m:
        return True
    else:
        return False
def valid_day(user_day):
    if user_day.isdigit() and 1<=int(user_day)<=31:
        return True
    else:
        return False

def valid_year(user_year):
    if user_year.isdigit() and 1900<=int(user_year)<=2020:
        return True
    else:
        return False
#implement the function escape_html(),with replace > < " and &
def escape_html(s):
    for (i,o) in (("&","&amp;"),(">","&gt;"),('<',"&lt;"),('"','&quot;')):
        s=s.replace(i,o)
    return s
    # cgi.escape(s,quote=True)



form="""
<form method='post'>
    what is your birthday?
    <br>
    <label>Month
    <input type='text' name='month'>
    </label>
    <label>Day
    <input type='text' name='day'>
    </label>
    <label>Year
    <input type='text' name='year'>
    </label>
    <div style="color:red">%(error)s</div>
    <br>
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error=''):
        self.response.out.write(form % {"error":error})
    def get(self):
        #self.response.headers['Content-Type']='text/plain'
        self.write_form()
        #self.response.out.write('Hello world!')
    #add a post function to show the birthday correctly
    def post(self):
        user_month=self.request.get('month')
        month=valid_month(user_month)
        user_day=self.request.get('day')
        day=valid_day(user_day)
        user_year=self.request.get('year')
        year=valid_year(user_year)

        if not (month and day and year):
            self.write_form("Invalid birthday!")
            #self.response.out.write("Invalid Birthday! %s" % error)
        else:
            self.response.out.write("Thanks!That is totally a valid date.")


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
#
# google app engine hello world

#import webapp2
#class MainPage(webapp2.RequestHandler):
#    def get(self):
#        self.reponse.headers['Content-Type']='text/plain'
#        self.response.out.write('hello, webapp world!')
#app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
