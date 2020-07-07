'''
Created on Jul 6, 2020

@author: gabez
'''
from flask.wrappers import Response
import json
class Vital(Exception):
    def __init__(self, vital_signs, message='Failed to record vital signs'):
        self.vital_signs = vital_signs
        self.message = message
        response_message = vital_signs
        response_message['message'] = message
        return Response(json.dumps(response_message),status=500, mimetype='application/json')
        