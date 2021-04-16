#Import Flask
from flask import Flask, jsonify

#Dependencies
import numpy as np 
import datetime as datetime

#SQL toolkit
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.pool import StaticPool

