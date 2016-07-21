import numpy as np

from flask import Flask, abort, jsonify, request

import cPickle as pickle

#modelCol = pickle.load(open('./model/model_20160718.dump'))
#model = modelCol[0]
#columns = modelCol[1]

# print columns

my_random_forest = pickle.load(open("../iris.dump", "rb"))

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World!!</h1>"



@app.route('/api', methods=['POST'])
def iris_predict():
    #if request.method == 'POST':
    #    return "ECHO: POST\n"
    
    data = request.get_json(force=True)
    
    
    
    predict_request = [data['sl'], data['sw'], data['pl'], data['pw']]
    predict_request = np.array(predict_request)
    y_hat = my_random_forest.predict(predict_request)
    output = [y_hat[0]]
    return jsonify(results=output), 201


@app.route('/hello', methods=['POST'])
def make():
    """
     JSON should look like this
    {"firstName":"John",
    "lastName":"Snow",
    "knows":"nothing"}
    """
    
    # get data, xform to a dict of  pandas series
    data = request.get_json(force=True)

    # this is just a silly example
    firstName = data['firstName']
    lastName = data['lastName']
    knows = data['knows']

    results_dict = dict()
    results_dict['response'] = "Hello " + firstName + " " + lastName + ". I hear that you know " + knows

    # return the json
    return jsonify(results=results_dict)
    

# @app.route('/todo/api/v1.0/tasks', methods=['POST'])
@app.route('/sur_predict', methods=['POST'])
def make_predict():
    # all kinds of error checking should be here
    print 'inside'
    data = request.get_json(force=True)
    # convert our json to a numpy array
    predict_request = [data[col] for col in columns]
    predict_request = np.array(predict_request)
    predict = model.predict(predict_request)
    
    # return model prediction
    output = [predict[0]]
    return jsonify(results=output)


@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

 
if __name__ == '__main__':
    app.run(port=9000, debug=True)



