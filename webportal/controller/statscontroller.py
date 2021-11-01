from flask_restful import Resource, reqparse
from webportal.models.carstats import *


parser = reqparse.RequestParser()
parser.add_argument('mac_addr', required=True)
parser.add_argument('temperature', required=True)
parser.add_argument('battery_level', required=True)
parser.add_argument('distance', required=True)
parser.add_argument('speed', required=True)
parser.add_argument('line_detected', required=True)


class CarStatsControllerAPI(Resource):
    # The car creates a new entry by POST
    def post(self):
        args = parser.parse_args()
        insert_stats(args['mac_addr'], args['temperature'], args['battery_level'], 
            args['distance'], args['speed'], args['line_detected'])
        return "success", 201


    def display_dashboard_stats(self):
        stats = get_stats() 
        return stats


    def delete(self):
        pass 

# curl http://localhost:5000/car/stats -d "mac_addr=12345" -d "temperature=27.5" -d "battery_level=50" -d "distance=10" -d "speed=5" -d "line_detected=0" -X POST
# 