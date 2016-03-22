#!/usr/bin/pythonRoot

import RPi.GPIO as GPIO
from flup.server.fcgi import WSGIServer
import sys
import urlparse

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

def app(environ, start_response):
  # start our http response
  start_response("200 OK", [("Content-Type", "text/html")])
  # look for inputs on the URL
  i = urlparse.parse_qs(environ["QUERY_STRING"])
  yield ('&nbsp;') # flup expects a string to be returned from this function
  # if there's a url variable named 'q'
  if "q" in i:
    if i["q"][0] == "w":
      GPIO.output(25, True)   # Turn it on
    elif i["q"][0] == "s":
      GPIO.output(25, False)  # Turn it off

#by default, Flup works out how to bind to the web server for us, so just call i$
WSGIServer(app).run()
