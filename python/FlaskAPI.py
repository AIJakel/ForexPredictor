from flask import Flask, jsonify, request
import operationsAPI, predictWithTransform
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import load_model

app = Flask(__name__)
def init():
    global model,graph
    # load the pre-trained Keras model
    model = load_model('model_predictFutureCandle.model')
    graph = tf.get_default_graph()

@app.route('/historical/<string:curr_Pair>', methods=['GET'])
def get_AllHistorical(curr_Pair):
    return operationsAPI.getAllHistorical(curr_Pair)

# @app.route('/prediction/<string:curr_Pair>', methods=['GET'])
# def get_Prediction(curr_Pair):
#     return operationsAPI.getPrediction(curr_Pair)

@app.route('/prediction/<string:curr_Pair>', methods=['GET'])
def get_Prediction(curr_Pair):
    inputFeature = operationsAPI.getPredictionData(curr_Pair)
    with graph.as_default():
        raw_prediction = model.predict(inputFeature)
    
    prediction = pd.DataFrame(raw_prediction, columns=["1","2","3","4"])
    return prediction.to_json(orient='records')
    
@app.route("/")
def helloWorld():
    return jsonify({"Status":"Test"})

if __name__ == "__main__":
    init()
    app.run(threaded=True, debug=True)