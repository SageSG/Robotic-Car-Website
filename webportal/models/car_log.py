from webapp import db


class CarLogs(db.Model):
    distance = db.Column(db.Float, nulllabe=False)
    speed = db.Column(db.Float, nulllabe=False)
    line_detected = db.Column(db.Boolean, nulllabe=False)
    response_code = db.Column(db.Int, nulllabe=False)


    def __init__(self, distance, speed, line_detected, response_code):
        self.distance = distance
        self.speed = speed
        self.line_detected = line_detected
        self.response_code = response_code


def insert_log(distance, speed, line_detected, response_code):
    row = CarLogs(distance, speed, line_detected, response_code)

    try:
        db.session.add(row)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return True


def retrieve_log(self):
    pass