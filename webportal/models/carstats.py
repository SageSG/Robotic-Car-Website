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


def get_car_stats():
    # Retrieve the latest stats from the DB
    data = db.session.query(CarStats).order_by('id').all()

    # Latest entry data 
    latest_entry = data[-1]
    current_speed = latest_entry.speed
    current_temps = latest_entry.temperature
    current_stats = {'current_speed': current_speed, 'current_temps': current_temps}

    # For tempature graph 
    temps_graph_stats = {}
    counter = 1 
    movement_placeholder = f"Movement {counter}"
    for item in data:
        movement_placeholder = f"Movement {counter}"
        temps_graph_stats[movement_placeholder] = item.temperature
        counter += 1

    # For rate of line detection graph 
    line_detect_graph_stats = {}
    counter = 1
    movement_placeholder = f"Movement {counter}"
    for item in data:
        movement_placeholder = f"Movement {counter}"
        line_detect_graph_stats[movement_placeholder] = item.line_detected    
        counter += 1

    # Line detection count graph 
    line_count_graph_stats = {}
    true_count = 0
    false_count = 0 
    for item in data:   
        if item.line_detected == 1:
            true_count += 1 
        else:
            false_count += 1 
    line_count_graph_stats["true_count"] = true_count
    line_count_graph_stats["false_count"] = false_count  

    return current_stats, temps_graph_stats, line_detect_graph_stats, line_count_graph_stats


def reset():
    # Remove all entires in the DB
    num_rows_deleted = db.session.query(CarStats).delete()
    db.session.commit()