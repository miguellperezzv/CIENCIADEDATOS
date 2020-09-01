# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 06:32:15 2019

@author: jairo
"""
import buscador_twitter as bt
from flask import Flask
from flask import render_template

import pandas as pd


app=Flask(__name__)

@app.route('/')

def saludar():
    return render_template('ventana.html')

if __name__=='__main__':
    app.run(port=5000,debug=True)


