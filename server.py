"""Master Productivity Tracker"""

# -*- coding: utf-8 -*-
from __future__ import print_function
from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, flash, session, g
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Time, Activity
from sqlalchemy import and_
from datetime import datetime
import sys


app = Flask(__name__)

app.config.update(
    PROPAGATE_EXCEPTIONS = True
)

app.secret_key = 'secret'

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
	"""Homepage"""

	times = db.session.query(Time).all()

	return render_template('homepage.html', times=times)

@app.route('/schedule')
def schedule():
	"""Schedule template"""

	return render_template('schedule.html')

@app.route('/schedule.json')
def get_schedule():
	"""Generates schedule for the day"""

	start_time_id = request.args.get('start_time_id')
	end_time_id = request.args.get('end_time_id')

	schedule_times = db.session.query(Time.str_time, Time.time_id).filter(and_(Time.time_id>=start_time_id,
														Time.time_id<=end_time_id)).all()

	times_to_send = {'times': schedule_times}

	return jsonify(times_to_send)

@app.route('/save.json')
def save_schedule():
	"""Saves schedule to database"""

	activities = request.args.getlist('activities[]')
	times = request.args.getlist('times[]')
	day = request.args.get('date').split(" ")
	serialized_date = "{}/{}/{}".format(day[1], day[2], day[3])
	formatted_date = datetime.strptime(serialized_date, '%b/%d/%Y')


	for i in range(len(activities)):
		new_activity = Activity(name=activities[i], time=times[i], date=formatted_date)
		print(new_activity, file=sys.stderr)
        db.session.add(new_activity)

	db.session.commit()
	

	return "success"


if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    connect_to_db(app) 
    DebugToolbarExtension(app)

    app.run(host="127.0.0.1")
