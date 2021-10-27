import json
from webportal import db

class CarStats(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    mac_addr = db.Column(db.String(12))
    temperature = db.Column(db.Float)
    battery_level = db.Column(db.Integer)
    distance = db.Column(db.Float)
    speed = db.Column(db.Float)
    line_detected = db.Column(db.Boolean)


    def __init__(self, mac_addr, temperature, battery_level, distance, speed, line_detected):
        self.mac_addr = mac_addr
        self.temperature = temperature
        self.battery_level = battery_level
        self.distance = distance
        self.speed = speed
        self.line_detected = int(line_detected)


def insert_stats(mac_addr, temperature, battery_level, distance, speed, line_detected):
    # Inserts the stats sent from the car to the DB
    car_stats = CarStats(mac_addr, temperature, battery_level, distance, speed, line_detected)
    db.session.add(car_stats)
    db.session.commit()


def get_stats():
    # Retrieve the latest stats from the DB
    largest_id = db.session.query(CarStats).order_by('id').all()[-1].id
    stats = CarStats.query.filter_by(id=largest_id).first()
    stats_json = {'mac_addr': stats.mac_addr, 'temperature': stats.temperature, 
    'battery_level': stats.battery_level, 'distance': stats.distance, 
    'speed': stats.speed, 'line_detected': stats.line_detected}
    return stats_json
