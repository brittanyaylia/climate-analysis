#mport Flask
from flask import Flask, jsonify

#dependencies
import numpy as np 
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.pool import StaticPool

#create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#reflect existing db & tables
Base = automap_base()
Base.prepare(engine, reflect=True)

#save to tables
measure = Base.classes.measurement
station = Base.classes.station
Session = Session(engine)

#create app
app = Flask(__name__)

#home route
@app.route("/")

def welcome():
    return(
        f"Climate API Homepage<br/>"
        f"Routes: <br/>"
        f"f/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

#precipitation route
@app.route("/api/v1.0/precipitation")
def orecipitation():
    one_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    prcp = Session.query(measure.date, measure.prcp).\
        filter(measure.date >= one_year).\
        order_by(measure.date).all()
    prcp_list = dict(prcp)

    return jsonify(prcp_list)

#station route
@app.route("/api/v1.0/stations")
def stations():
    stations = Session.query(station.station, station.name).all()
    stations_list = list(stations)

    return jsonify(stations_list)

#TOBs route
@app.route("/api/v1.0/tobs")
def tobs():
    one_year = dt.date(2017, 8, 23) - dt.timedelta(days= 365)
    tobs_data = Session.query(measure.date, measure.tobs).\
        filter(measure.date >= one_year).\
        order_by(measure.date).all()
    tobs_list = list(tobs_data)

    return jsonify(tobs_list)

#start route
@app.route("/api/v1.0/<start>")
def start_date(start):
    start_date = Session.query(measure.date, func.min(measure.tobs), func.avg(measure.tobs), func.max(measure.tobs)).\
        filter(measure.date >= start).\
        group_by(measure.date).all()
    start_list = list(start_date)

    return jsonify(start_list)

#start/end route
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    start_end = Session.query(measure.date, func.min(measure.tobs), func.avg(measure.tobs), func.max(measure.tobs)).\
        filter(measure.date >= start).\
        filter(measure.date <= end).\
        group_by(measure.date).all()
    start_end_list = list(start_end)

    return jsonify(start_end_list)
