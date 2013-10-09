#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

print "Content-type: text/html"
print

print """
<html>
<head>
<title>Hello World!</title>
<style>
#wrap{
margin:auto;
width:90%;
height:100%;
background-color:#f2f2f2;
padding:2%;

}
body{
margin:0;
border:0;
width:100%;
height:auto;
background-color:#0099FF;
}
#hello{
overflow-y:scroll;
padding:1%;
width:100%;
height:70%;
}
</style>
</head>
<body>
<div id='wrap'>
<h2>Hello world!</h2><hr>
<p>
I feel strongly that in modern day computing lessons, the world doesn't get greeted enough! So this is a for loop in range of 1024 to make sure the world gets greeted! :D </br>
<div id='hello'>
"""
for i in range(0,1024):
	print "Hello world! </br>"
print """
</div>
</p>
</div>
</body>
</html>
"""
