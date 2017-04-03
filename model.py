from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#####################################################
# Model Defintions

# class Time(db.Model):
# 	"""Times of day, in 15 minute chunks"""

# 	__tablename__ = 'times'

# 	time_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
# 	time = db.Column(db.Time(timezone=False), nullable=False)
# 	str_time = db.Column(db.String(100), nullable=False)

# 	def __repr__(self):
# 		"""Provides a representation of times"""

# 		return '<Time time = {}>'.format(self.time)


class Category(db.Model):
	"""Categories of activities to do"""

	__tablename__ = 'categories'

	category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	bucket_name = db.Column(db.String(200), nullable=False)
	category_name = db.Column(db.String(200), nullable=False)
	hours = db.Column(db.Integer)
	color = db.Column(db.String(10), nullable=False)


	def __repr__(self):
		"""Provides a repesentation of activities"""

		return '<Category category_name = {}>'.format(self.category_name)

class Activity(db.Model):
	"""Activities planned for a given day"""

	__tablename__ = 'activities'

	activity_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
	activity_name = db.Column(db.String(200), nullable=False)

	category = db.relationship('Category', backref=db.backref('activities', 
                                                                      order_by=activity_id))

	def __repr__(self):
		"""Provides a repesentation of activities"""

		return '<Activity activity_name = {} category = {}>'.format(self.activity_name, self.category_id)

def connect_to_db(app, db_uri='postgresql:///todo'):
    """Connect the database to Flask app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."


