from app import create_app, db, socketio
from app.creastimate.models import User

# --------local testing----------------
if __name__ == "__main__":
    flask_app = create_app('dev')
    with flask_app.app_context():
        db.create_all()
    flask_app.run()
# ------------------------------------------

#-----------------PRODUCTION---------------------
# flask_app = create_app('prod')
#
# with flask_app.app_context():
#     db.create_all()
#     try:
#         if not User.query.filter_by(user_name='harry').first():
#             User.create_user(user='harry', email='harry@potters.com', password='secret')
#     except exc.IntegrityError:
#         # socketio = SocketIO(flask_app)
#         socketio.run(flask_app)