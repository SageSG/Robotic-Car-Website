class RoboticCar(db.Model):
    car_mac = db.Column(db.String(12), primary_key = True)
    speed = db.Column(db.Integer)
    temp = db.Column(db.Float)
    rps = db.Column(db.Integer)
    battery = db.Column(db.Integer)

    def __init__(self):
        self.car_mac = str(car_mac).upper()
        self.speed = int(speed)
        self.temp = float(temp)
        self.rps = int(rps)
        self.battery = int(battery)

#def get_car_mac()
#def update_speed
#def update_temp
#def update_rps
#def update_battery