from datetime import timedelta

from flask_restful import Api

from config import run_config
from flask import Flask

from create_db import CreateDB, create_db
from db import db, migrate
from routes.rooms import rooms_bp, GetRooms
from routes.staff import staff_bp, GetStaff, StaffRoom
from routes.tenants import tenants_bp, GetTenants

app = Flask(__name__)
api = Api(app)

app.config.from_object(run_config())

db.init_app(app)
migrate.init_app(app, db)

app.permanent_session_lifetime = timedelta(minutes=20)


app.register_blueprint(create_db)
app.register_blueprint(rooms_bp)
app.register_blueprint(staff_bp)
app.register_blueprint(tenants_bp)

api.add_resource(CreateDB, "/create_db")
api.add_resource(GetRooms, '/rooms', '/rooms/<int:room_id>')
api.add_resource(GetStaff, '/staff', '/staff/<int:staff_id>')
api.add_resource(GetTenants, '/tenants', '/tenants/<int:tenant_id>')
api.add_resource(StaffRoom, "/staff_room")

