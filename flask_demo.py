import numpy as np

from flask import Flask, abort, jsonify, request

import cPickle as pickle

my_model = pickle.load(open('./model/model_20160718.dump'))

app = Flask(__name__)

@app.route('/sur_predict', methods=['POST'])
def make_predict():
    # all kinds of error checking should be here
    data = request.get_json(force=True)
    # convert our json to a numpy array
    predict_request = [data['sl']]
    predict_request = np.array(predict_request)
