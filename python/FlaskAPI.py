from flask import Flask, jsonify, request
import operationsAPI, getPredictionData
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import load_model

#This file contains all the api information

#initalizes the tensorflow graph (needed for tf to work with flask)
app = Flask(__name__)
def init():
    global model,graph
    # load the pre-trained Keras model
    model = load_model('model_predictFutureCandle.model')
    graph = tf.get_default_graph()

# end point for getting all the historic data for a specified pair
@app.route('/historical/<string:curr_Pair>', methods=['GET'])
def get_AllHistorical(curr_Pair):
    return operationsAPI.getAllHistorical(curr_Pair)

#end point for getting the prediction for the next hour for a specified pair
@app.route('/prediction/<string:curr_Pair>', methods=['GET'])
def get_Prediction(curr_Pair):
    inputFeature = operationsAPI.getCurrData(curr_Pair)
    with graph.as_default():
        raw_prediction = model.predict(inputFeature)
    
    prediction = pd.DataFrame(raw_prediction, columns=["p_open","p_close","p_high","p_low"])
    return prediction.to_json(orient='records')

#test api end point
@app.route("/")
def helloWorld():
    return "Hellow World" #jsonify({"Status":"Test"})

if __name__ == "__main__":
    init()
    app.run(threaded=True, debug=True, host='0.0.0.0')