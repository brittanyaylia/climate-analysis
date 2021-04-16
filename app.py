#Import Flask
from flask import Flask, jsonify

#Dependencies
import numpy as np 
import datetime as datetime
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.pool import StaticPool

#Create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflect existing db & tables
Base = automap_base()
Base.prepare(engine, reflect=True)

#Save references to tables
measure=Base.classes.measurement
station = Base.classes.station
Session = Session(engine)

#Create app
app = Flask(__name__)

