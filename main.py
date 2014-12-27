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
from validation import valid_month, valid_day, valid_year, escape_html
import logging


form = """
<form method="post">
	<h1>Enter text to ROT13</h1>
	<br>
	<label>
		<textarea name="text" rows=5 cols=35 value="%(text)s"></textarea>
	</label>

	<div style="color: red">%(error)s</div>	
	<br>
	<br>
	<input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    
    def write_form(self, error="", text=""):
    	self.response.out.write(form % {"error" : error, "text" : escape_html(text)})

    def get(self):
        self.write_form()

    def post(self):
    	user_text = self.request.get('text')
    	logging.info("value of text is %s", user_text)
    	text = escape_html(user_text)
    	self.write_form("", text)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
