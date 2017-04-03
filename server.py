"""Master Productivity Tracker"""

# -*- coding: utf-8 -*-
from __future__ import print_function
from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, flash, session, g
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Activity, Category
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

@app.route('/lookup.json')
def look_up():
	"""Checks if a typed activity is already categorized in the database"""


	typed_activity = request.args.get('activity', 0, type=str)

	matching_activity = db.session.query(Activity).filter(Activity.activity_name==typed_activity).all()

	return jsonify(matching_activity)


if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    connect_to_db(app) 
    DebugToolbarExtension(app)

    app.run(host="127.0.0.1")
