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
@app.route("/cal/res/<int:val1>/<int:val2>")
def res(val1, val2):
    reps = "La respuesta de {} - {} = {}\n".format(val1, val2, val1-val2)
    logger.info(reps)
    return reps

#////////////__MULTI__/////////////////////////////////////////////////#
@app.route("/cal/mul/<int:val1>/<int:val2>")
def mul(val1, val2):
    reps = "La respuesta de {} * {} = {}\n".format(val1, val2, val1*val2)
    logger.info(reps)
    return reps


#////////////__DIV__/////////////////////////////////////////////////#
@app.route("/cal/div/<int:val1>/<int:val2>")
def div(val1, val2):
    reps = "La respuesta de {} / {} = {}\n".format(val1, val2, val1/val2)
    logger.info(reps)
    return reps


#////////////__XXXX__/////////////////////////////////////////////////#
#----------------------------------------------------------------
