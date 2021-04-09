#!/usr/bin/env python3

import os
from flask import Flask
import names

app = Flask(__name__)

@app.route('/')
def hello():
  return ("Hello, "+names.get_full_name())

@app.route('/populate')
def populate():
  return ("inserting datas ... NOT")

if __name__ == '__main__':
  app.run(host="0.0.0.0",port="5000")

