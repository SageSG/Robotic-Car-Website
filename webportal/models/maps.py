# Map id, Can_move, got obstacle 


class Maps(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    map_coordinates = db.Column(db.String)


    def __init__(self, map_coordinates):
        self.map_coordinates = map_coordinates


def insert_map():
	pass 


def get_map():
	pass 
