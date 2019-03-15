from flask import Flask, jsonify, request
import operationsAPI, predictWithTransform

app = Flask(__name__)

@app.route('/historical/<string:curr_Pair>', methods=['GET'])
def get_AllHistorical(curr_Pair):
    return operationsAPI.getAllHistorical(curr_Pair)

@app.route('/prediction/<string:curr_Pair>', methods=['GET'])
def get_Prediction(curr_Pair):
    return operationsAPI.getPrediction(curr_Pair)

@app.route("/")
def helloWorld():
    return jsonify({"Status":"Test"})

if __name__ == "__main__":
    app.run(debug=True)