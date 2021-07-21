import flask
from flask import request, jsonify
from random import *


app = flask.Flask(__name__)
app.config["DEBUG"] = True

def obl_strategy():
    with open('sources/oblique-strategies.txt', 'r') as ost:
        strats = ost.readlines()
        length = len(strats)
    idx = randint(0, length)
    strat = strats[idx].strip()
    return strat


def acute_strategy():
    with open('sources/acute-strategies.txt', 'r') as ost:
        strats = ost.readlines()
        length = len(strats)
    idx = randint(0, length)
    strat = strats[idx].strip()
    return strat

def i_ching():
    with open('sources/i-ching.txt', 'r') as ost:
        strats = ost.readlines()
        length = len(strats)
    idx = randint(0, length)
    strat = strats[idx].strip()
    return strat

@app.route('/', methods=['GET'])
def home():
    oblique = obl_strategy()
    acute = acute_strategy()
    iching = i_ching()
    return f'<div style ="margin: auto; width: 50%; border: 3px solid green; padding: 10px; text-align: center"><h2>{iching}</h2><h4>{oblique}</h4><h4>{acute}</h4></div>'


@app.route('/api', methods=['GET'])
def api():
    oblique = obl_strategy()
    acute = acute_strategy()
    iching = i_ching()
    obj_return = {
        'i-ching': iching,
        'oblique-strategy': oblique,
        'acute-strategy': acute
    }
    return jsonify(obj_return)

app.run()
