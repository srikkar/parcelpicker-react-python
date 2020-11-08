# -*- coding: utf-8 -*-
from flask import Flask, jsonify, make_response, send_from_directory
from flask.globals import request
from flask_jsonschema_validator import JSONSchemaValidator
import json
import os
import jsonschema
import logging
import logging.config

LOG_FILE_NAME = 'logging.conf'
logging.config.fileConfig(os.path.join(os.path.dirname(os.path.realpath(__file__)), "conf", LOG_FILE_NAME))

# create logger
logger = logging.getLogger('PackageSolutionService')

app = Flask(__name__)
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

print("ROOT_PATH:::"+ROOT_PATH)
app = Flask(__name__,static_folder=ROOT_PATH+"/view/parcel-parser/build/static")
JSONSchemaValidator(app=app, root="schemas")
"""  """
try:
    from utils import parcelParser

except Exception as error:
    logger.error(error)


""" App Routing """
@app.route('/package-solution',defaults={'path': ''}, methods=['GET'])
@app.route('/package-solution', methods=['GET'])
def index():
    """ static files serve """
    logger.debug("direct:: from "+ROOT_PATH)
    return send_from_directory(os.path.join(ROOT_PATH,"view/parcel-parser/build"), 'index.html')

@app.route('/package-solution/<path:path>',  methods=['GET'])
def static_proxy(path):
    """ static folder serve """
    file_name = path.split('/')[-1]
    logger.debug(file_name)
    logger.debug(path)
    logger.debug(path.split('/')[:-1])
    dir_name = os.path.join(ROOT_PATH,"view/parcel-parser/build", '/'.join(path.split('/')[:-1]))
    logger.debug(dir_name)
    return send_from_directory(dir_name, file_name)



@app.route('/parseTheParcel/checkAlive', methods=['GET'])
def checkAlive():
    try:
        return make_response(jsonify(status='live'), 200)
    except Exception as error:
        logger.error(error)
        return make_response(jsonify(error=str(error)), 500)


@app.route('/parseTheParcel/weightLimit', methods=['GET'])
def weightLimit():
    try:
        packageSolutionObj = parcelParser.ParcelParser(logger=logger)
        return app.response_class(
            response=json.dumps(
                {'weightLimit': packageSolutionObj.thresholdWeight.get('value'),
                 'unit': packageSolutionObj.thresholdWeight.get('unit')}),
            status=200, mimetype='application/json')
    except Exception as error:
        logger.error(error)
        return make_response(jsonify(error=str(error)), 500)


@app.route('/parseTheParcel/packageTypes', methods=['GET'])
def packageTypes():
    try:
        packageSolutionObj = parcelParser.ParcelParser(logger=logger)
        return app.response_class(
            response=json.dumps(
                {'packages': packageSolutionObj.envConfig.get('packages', []),
                 'unit': packageSolutionObj.envConfig.get('packageDimensionUnit')}),
            status=200, mimetype='application/json')
    except Exception as error:
        logger.error(error)
        return make_response(jsonify(error=str(error)), 500)


@app.route('/parseTheParcel/checkWeight', methods=['POST'])
@app.validate('packageSolution', 'weight')
def checkWeight():
    try:
        packageSolutionObj = parcelParser.ParcelParser(logger=logger)
        if packageSolutionObj.checkWeight(request.json['weight']):
            return make_response(jsonify(message='Allowed'), 200)
        else:
            return make_response(jsonify(message='Not Allowed'), 200)
    except Exception as error:
        logger.error(error)
        return make_response(jsonify(error=str(error)), 500)


@app.route('/parseTheParcel/packageSolution', methods=['POST'])
@app.validate('packageSolution', 'dimensions')
def packageSolution():
    try:
        packageSolutionObj = parcelParser.ParcelParser(logger=logger)
        outputDict = packageSolutionObj.getpackageSolution(request.json)
        return app.response_class(response=json.dumps(outputDict),
                                      status=200,
                                      mimetype='application/json')

    except Exception as error:
        logger.error(error)
        return make_response(jsonify(error=str(error)), 500)


@app.errorhandler(jsonschema.ValidationError)
def onValidationError(error):
    return make_response(jsonify(error=str(error.message)), 400)


if __name__ == '__main__':
    logger.info("Starting package Solution Service...")
    if os.getenv('ENV', 'DEV') == "DEV":
        from flask_cors import CORS
        CORS(app)
        app.run(host="127.0.0.1", port="8001", debug=True)
    else:
        app.run(host="127.0.0.1", port="8001")

