from model import Activity, Category, connect_to_db, db
from server import app
from datetime import datetime
import csv

# def load_times():
# 	"""Loads times from times.csv"""
# 	print 'Times'

# 	Time.query.delete()

# 	#reads file and inserts data
# 	with open('seed_data/times.csv', 'rb') as csvfile:
# 		times = csv.reader(csvfile, delimiter=',')
# 		for t in times:
# 			t = str(t)
# 			formatted_time = datetime.strptime(t[2:-2], '%H:%M')
# 			db_time = Time(time=formatted_time, str_time=t[2:-2])
# 			db.session.add(db_time)
# 		db.session.commit()


def load_categories():
	print "Categories"

	Category.query.delete()

	with open('seed_data/categories.csv', 'rb') as categories_csvfile:
		categories = csv.reader(categories_csvfile, delimiter=',')
		for c in categories:
			bucket, category, hours, color = c
			db_category = Category(bucket_name=bucket, category_name=category, hours=hours, color=color)
			db.session.add(db_category)
		db.session.commit()

def load_activities():
	print "Activities"

	Activity.query.delete()

	with open('seed_data/activities.csv', 'rb') as activities_csvfile:
		activities = csv.reader(activities_csvfile, delimiter=',')
		for a in activities:
			category_id, name = a
			db_activity = Activity(category_id=category_id, activity_name=name)
			db.session.add(db_activity)
		db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()
    load_categories()
    load_activities()