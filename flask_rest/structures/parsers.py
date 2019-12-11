from flask_restful import reqparse


pars_room = reqparse.RequestParser()
pars_room.add_argument('room_id', type=int)

staff_room_parser = reqparse.RequestParser()
staff_room_parser.add_argument('number', type=int)

pars_staff = reqparse.RequestParser()
pars_staff.add_argument('staff_id', type=int)


pars_tenants = reqparse.RequestParser()
pars_tenants.add_argument('tenant_id', type=int)
