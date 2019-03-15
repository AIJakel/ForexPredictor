from flask import Flask, jsonify, request
import operationsAPI

app = Flask(__name__)

@app.route('/historical/<string:curr_Pair>', methods=['GET'])
def get_AllHistorical(curr_Pair):
    return operationsAPI.getAllHistorical(curr_Pair)

@app.route('/historical/<string:curr_Pair>&<string:date_Time>', methods=['GET'])
def get_SelectHistorical(curr_Pair, date_Time):
    return jsonify({"Status":"NOT IMPLEMENTED"})

@app.route("/")
def helloWorld():
    return jsonify({"Status":"Test"})

if __name__ == "__main__":
    app.run(debug=True)