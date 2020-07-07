'''
Created on Jul 6, 2020

@author: gabez
'''
from flask.blueprints import Blueprint

pi_info = Blueprint('pi_info', __name__, url_prefix='/pi')
admin = Blueprint('admin', __name__, url_prefix='/admin')