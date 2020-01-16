from flask import Blueprint


creastimate_main = Blueprint('creastimate_main', __name__ , template_folder='templates')

from app.creastimate import routes
