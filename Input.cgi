#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import cgi
cgitb.enable()

print "Content-type: text/html"

print """
<html>

<head><title>Sample CGI Script</title></head>

<body>

  <h3> Get form data using python </h3>
"""

form = cgi.FieldStorage()
message = form.getvalue("message", "NULL")

print """

  <p>Previous message: <strong> %s </strong></p>

  <form method="post" action="">
    <p>Input: <input type="text" name="message"/></p>
  </form>

</body>

</html>
""" % cgi.escape(message)
