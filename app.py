#!/usr/bin/python3
# -*- coding: utf-8 -*-

from asyncio.log import logger
from flask import Flask
#app = flask.Flask(app)

import logging

logging.basicConfig(
    filename="uneti.log",
    format='%(asctime)s %(message)s',
    filemode='w'
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


app = Flask(__name__)

#////////////__SUMA__/////////////////////////////////////////////////#
@app.route("/cal/sum/<int:val1>/<int:val2>")
def sum(val1, val2):
    rep = "La respuesta de {} + {} = {}\n".format(val1, val2, val1+val2)
    logger.info(rep)
    return rep
    
#\n
#////////////__RESTA__/////////////////////////////////////////////////#
@app.route("/cal/res/<int:val3>/<int:val4>")
def res(val3, val4):
    reps = "La respuesta de {} - {} = {}\n".format(val3, val4, val3-val4)
    logger.info(reps)
    return reps 
    

#////////////__MULTI__/////////////////////////////////////////////////#
@app.route("/cal/mul/<int:val5>/<int:val6>")
def mul(val5, val6):
    reps = "La respuesta de {} * {} = {}\n".format(val5, val6, val5*val6)
    logger.info(reps)
    return reps
    

#////////////__DIV__/////////////////////////////////////////////////#
@app.route("/cal/div/<int:val7>/<int:val8>")
def div(val7, val8):
    reps = "La respuesta de {} / {} = {}\n".format(val7, val8, val7/val8)
    logger.info(reps)
    return reps
    

#////////////__XXXX__/////////////////////////////////////////////////#
#----------------------------------------------------------------

#app = Flask(app.py)

#@app.route('/')
#def hello_world():
#   return 'Hello, World!'
