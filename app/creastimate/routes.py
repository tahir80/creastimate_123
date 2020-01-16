from app.creastimate import creastimate_main as cm
from app.creastimate.models import User
from app import create_app, db
from sqlalchemy import exc,asc, desc, and_, or_
import datetime

from flask import session as login_session, json
import requests
# from app.auth import authentication as at
from flask_login import login_required
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, request, redirect, url_for, flash # for flash messaging


from app import socketio

from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect


@cm.route('/')
def demographics():
    return render_template("index.html")

@cm.route('/input')
def input():
    return render_template("one.html")

@cm.route('/output')
def output():
    return render_template("two.html")

@cm.route('/create')
def create():
    return render_template("three.html")
