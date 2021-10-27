from webportal import db

class CarCommands(db.Model):
	id = db.Column(db.Integer , primary_key=True)
	direction = db.Column(db.String(20))
	command = db.Column(db.Integer)

	def __init__(self, direction, command):
		self.direction = direction
		self.command = command 


def insert_commands(command):
    # Inserts the commands to the db 
    command = CarCommands("car", command)
    db.session.add(command)
    db.session.commit()


def get_commands():
	# Get the commands from the db and send it to the car (ask HL or Jas)
	pass 


def reset():
	# Delete all entires in the database 
	pass 
	