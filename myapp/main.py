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

form="""
<form action="/testform">
    <input name='q'>
    <input type="submit">
</form>
"""
#action="http://google.com/search"   submit to google

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type']='text/plain'
        self.response.out.write(form)
        #self.response.out.write('Hello world!')
#multiple handlers

class TestHandler(webapp2.RequestHandler):
    def get(self):
        q=self.request.get("q")
        self.response.out.write(q)
        #self.response.headers['Content-Type']='text/plain'
        #self.response.out.write(self.request)    #print out HTTP request

app = webapp2.WSGIApplication([('/', MainHandler),("/testform", TestHandler)], debug=True)
#
# google app engine hello world

#import webapp2
#class MainPage(webapp2.RequestHandler):
#    def get(self):
#        self.reponse.headers['Content-Type']='text/plain'
#        self.response.out.write('hello, webapp world!')
#app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
