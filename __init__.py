from flask import Flask,jsonify, make_response,request
from functions import databaseentry, databaseread

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return ":) The data entry point is /entrypoint and exit point is /exitpoint"

@app.route('/entrypoint', methods=['GET'])
def entrypoint():
    ir=request.args.get("ir")
    hr=request.args.get("hr")
    output=databaseentry(ir, hr)
    return make_response(jsonify(output), 200)

@app.route('/exitpoint', methods=['GET'])
def exitpoint():
    output=databaseread()
    return make_response(jsonify(output), 200)
