from flask_restful import Resource, reqparse
from webportal.models.carcommands import *


parser = reqparse.RequestParser()
parser.add_argument('direction', required=True)
parser.add_argument('command', required=True)


class ControlsControllerAPI(Resource):
    def post(self):
    	args = parser.parse_args()
    	if args['command'] == "Forward ^":
    		args['command'] = 1

    	elif args['command'] == "Back ˅":
    		args['command'] = 2

    	elif args['command'] == "Left ":
    		args['command'] = 3

    	elif args['command'] == "Right ":
    		args['command'] = 4

    	if args['direction'] == "webportal":
    		insert_commands(args['command'])

    	elif args['direction'] == "car":
    		# portal to car (ask HL or Jas)
    		pass 
    	else:
    		return 404

    	return 200