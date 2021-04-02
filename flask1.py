#!/usr/bin/env python3

import os
from flask import Flask
import string
import random

def randomstring(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, stringLength))

app = Flask(__name__)

@app.route('/')
def hello():
  return ("Hello, "+randomstring())

@app.route('/populate')
def populate():
  return ("Hello, Populous !")

if __name__ == '__main__':
  app.run(host="0.0.0.0",port="5000")

