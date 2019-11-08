from flask import Flask, current_app
from flask_restful import Api

from config import run_config
from routes.rooms import GetRooms, rooms_bp
from routes.staff import staff_bp, GetStaff
from routes.tenants import GetTenants, tenants_bp


app = Flask(__name__)
api = Api(app)

app.config.from_object(run_config())


api.add_resource(GetRooms, '/rooms', '/rooms/<int:room_id>')
api.add_resource(GetStaff, '/staff', '/staff/<staff_id>')
api.add_resource(GetTenants, '/tenants', '/tenants/<tenant_id>')


app.register_blueprint(rooms_bp)
app.register_blueprint(staff_bp)
app.register_blueprint(tenants_bp)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=current_app.config["DEBUG"])
