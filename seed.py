from model import Time, connect_to_db, db
from server import app
from datetime import datetime
import csv

def load_times():
	"""Loads times from times.csv"""
	print 'Times'

	Time.query.delete()

	#reads file and inserts data
	with open('seed_data/times.csv', 'rb') as csvfile:
		times = csv.reader(csvfile, delimiter=',')
		for t in times:
			t = str(t)
			formatted_time = datetime.strptime(t[2:-2], '%H:%M')
			db_time = Time(time=formatted_time, str_time=t[2:-2])
			db.session.add(db_time)
		db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()
    load_times()