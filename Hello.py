# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:09:06 2019

@author: madhu
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

if __name__ == '__main__':
   app.debug = True
   app.run()
##app.run(debug = True)