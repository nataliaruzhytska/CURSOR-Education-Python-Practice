from datetime import timedelta

from flask_restful import Api

from config import run_config
from flask import Flask

from create_db.routes import CreateDB
from db import db
from routes.rooms import rooms_bp, GetRooms
from routes.staff import staff_bp, GetStaff, StaffRoom
from routes.tenants import tenants_bp, GetTenants

app = Flask(__name__)
api = Api(app)

app.config.from_object(run_config())

db.init_app(app)

app.permanent_session_lifetime = timedelta(minutes=20)

app.register_blueprint(rooms_bp)
app.register_blueprint(staff_bp)
app.register_blueprint(tenants_bp)

api.add_resource(GetRooms, '/rooms', '/rooms/<int:room_id>')
api.add_resource(GetStaff, '/staff', '/staff/<staff_id>')
api.add_resource(GetTenants, '/tenants', '/tenants/<tenant_id>')
api.add_resource(CreateDB, "/create_db")
api.add_resource(StaffRoom, "/staff_room")

if __name__ == '__main__':
    app.run()
