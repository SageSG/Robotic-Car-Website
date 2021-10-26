from webportal import db


class Car(db.Model):
    mac_addr = db.Column(db.String(12), primary_key = True)
    temperature = db.Column(db.Float, nulllabe=False)
    battery = db.Column(db.Integer, nulllabe=False)
    distance = db.Column(db.Float, nulllabe=False)
    speed = db.Column(db.Float, nulllabe=False)
    line_detected = db.Column(db.Boolean, nulllabe=False)
    response_code = db.Column(db.Int, nulllabe=False)


    # def __init__(self):
    #     self.car_mac = str(car_mac).upper()
    #     self.speed = int(speed)
    #     self.temp = float(temp)
    #     self.rps = int(rps)
    #     self.battery = int(battery)

    # update_car

def insert_stats(mac_addr, temperature, battery, distance, speed, line_detected, response_code):
    car = Car(mac_addr, temperature, battery, distance, speed, line_detected, response_code)
    db.session.add(car)
    db.session.commit()


def update_stats():
    pass


def check_connection(self):
    pass


#def get_car_mac()
#def update_speed
#def update_temp
#def update_rps
#def update_battery