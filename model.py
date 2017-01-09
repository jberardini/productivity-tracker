from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#####################################################
# Model Defintions

class Time(db.Model):
	"""Times of day, in 15 minute chunks"""

	__tablename__ = 'times'

	time_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	time = db.Column(db.Time(timezone=False), nullable=False)
	str_time = db.Column(db.String(100), nullable=False)

	def __repr__(self):
		"""Provides a representation of times"""

		return '<Time time = {}>'.format(self.time)

class Activity(db.Model):
	"""Activities planned for a given day"""

	__tablename__ = 'activities'

	activity_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	time = db.Column(db.Integer, db.ForeignKey('times.time_id'))
	date = db.Column(db.Date, nullable=False)

	def __repr__(self):
		"""Provides a repesentation of activities"""


def connect_to_db(app, db_uri='postgresql:///todo'):
    """Connect the database to Flask app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."


