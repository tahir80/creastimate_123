import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO
from flask_cors import CORS

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
socketio = SocketIO()

login_manager.login_view = 'authentication.do_the_login'
login_manager.session_protection = 'strong'

bcrypt = Bcrypt()

def create_app(config_type):

    app = Flask(__name__)
    CORS(app)

    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')

    app.config.from_pyfile(configuration)

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    socketio.init_app(app)

    from app.creastimate import creastimate_main
    app.register_blueprint(creastimate_main)

    return app
