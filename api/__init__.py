'''
Created on Jul 6, 2020

@author: gabez
'''
# from blueprints import api
from flask import request
from flask.blueprints import Blueprint
from flask import Response, abort
import json

api_bp = Blueprint('api',__name__, url_prefix='/api' )

@api_bp.route('/heartbeat', methods=['TRACE'])
def heatbeat():
    if request.method == 'TRACE':
        return Response('Beatting', status=200)
    else:
        return abort(405)

@api_bp.route('/vitals', methods=['POST'])
def vitals():
    if request.method == 'POST':
        try:
            return Response("Vitals recorded", status='200')
        except Exception as e:
            response_message = "vital_signs"
            response_message['message'] = 'Failed to record vital signs'
            return Response(json.dumps(response_message),status=500, mimetype='application/json')
    else:
        return abort(405)