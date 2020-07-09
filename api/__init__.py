#################################
# Created on Jul 6, 2020        #
#                               #
# @author: gabezter4            #
#################################
from flask import request
from flask.blueprints import Blueprint
from flask import Response, abort
import json
import traceback

api_bp = Blueprint('api',__name__, url_prefix='/api' )

@api_bp.route('/heartbeat', methods=['GET'])
def heatbeat():
    if request.method == 'GET':
        data = json.loads(request.data.decode('utf-8'))
        api_key = data['api-key']
        return Response('Beat', status=200)
    else:
        return abort(405)

@api_bp.route('/vitals', methods=['POST'])
def vitals():
    if request.method == 'POST':
        try:
            return Response("Vitals recorded", status='200')
        except Exception:
            response_message = "vital_signs"
            response_message['message'] = 'Failed to record vital signs'
            traceback.print_exc()
            return Response(json.dumps(response_message),status=500, mimetype='application/json')
    else:
        return abort(405)