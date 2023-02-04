from flask import Flask,request,jsonify,make_response
# from flask_cors import CORS, cross_origin
from flask_cors import CORS



from urlvalidator.func import *


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'This is my first API call!'


# @cross_origin()
@app.route('/urlresponse', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
    #  dictToReturn = {'url':input_json['url']}

     url = input_json["url"]
     urlcollec = fetchValidUrls(url)        
     urlresponses = getUrlResponses(urlcollec)
    #  response = make_response(jsonify(jsonify(urlresponses)), 200)

    #     # add the CORS header
    #  response.headers['Access-Control-Allow-Origin'] = '*'
    #  response.content_type = "application/json"

     return jsonify(urlresponses)
