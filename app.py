from flask import Flask,jsonify, make_response
from flask.globals import request
from flask_jsonschema_validator import JSONSchemaValidator
import json
import os
import jsonschema


app = Flask(__name__)
JSONSchemaValidator( app = app, root = "schemas" )

try:
    from utils import parcelParser
    
except Exception as error:
    print(error)

@app.route('/parseTheParcel/checkAlive', methods=['GET'])
def checkAlive():
    try:
        packageSolutionObj = parcelParser.ParcelParser()
        return make_response(jsonify(status='live'), 200)
    except Exception as error:
        print(error)
        return make_response(jsonify(error=str(error)), 500)


@app.route('/parseTheParcel/weightLimit', methods=['GET'])
def weightLimit():
    try:
        packageSolutionObj = parcelParser.ParcelParser()
        return app.response_class(response=json.dumps({'weightLimit': packageSolutionObj.thresholdWeight.get('value'), 'unit': packageSolutionObj.thresholdWeight.get('unit')}),
                            status=200,
                            mimetype='application/json')
    except Exception as error:
        print(error)
        return make_response(jsonify(error=str(error)), 500)

@app.route('/parseTheParcel/checkWeight', methods=['POST'])
@app.validate( 'packageSolution', 'weight' )
def checkWeight():
    try:
        packageSolutionObj = parcelParser.ParcelParser()
        if packageSolutionObj.checkWeight(request.json['weight']):
            return make_response(jsonify(message='Allowed'), 200)
        else:
            return make_response(jsonify(message='Not Allowed'), 200)
    except Exception as error:
        print(error)
        return make_response(jsonify(error=str(error)), 500)


@app.route('/parseTheParcel/packageSolution', methods=['POST'])
@app.validate( 'packageSolution', 'dimensions' )
def packageSolution():
    try:
        packageSolutionObj = parcelParser.ParcelParser()
        inputJson = request.json
        userInput = dict.fromkeys(['length','breadth', 'height'])
        for key in userInput:
            userInput[key] = inputJson[key]
        if checkWeight().json['message'] == "Allowed":
            print("userInput: "+str(userInput))
            return app.response_class(response=json.dumps(packageSolutionObj.checkDimensions(userInput)),
                            status=200,
                            mimetype='application/json')
        else:
            return make_response(jsonify(message='weight exceeded limit i.e., '+ str(packageSolutionObj.thresholdWeight.get('value'))+' '+ packageSolutionObj.thresholdWeight.get('unit')), 200)
    
    except Exception as error:
        print(error)
        return make_response(jsonify(error=str(error)), 500)

@app.errorhandler( jsonschema.ValidationError )
def onValidationError( error ):
  return make_response(jsonify(error=str(error.message)), 400)

if __name__=='__main__':
    print("Starting package Solution Service...")
    if os.getenv('ENV','DEV') == "DEV":
        from flask_cors import CORS
        CORS(app)
        app.run(host="127.0.0.1", port="8001", debug=True)