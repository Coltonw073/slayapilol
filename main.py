import requests
from flask import request
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)
@app.route("/get", methods=["GET"])
def postME():
    return requests.get(request.headers['URL']).text
if __name__ == "__main__":
   app.run(debug=False)
