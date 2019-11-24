from flask_restful import reqparse


pars_room = reqparse.RequestParser()
pars_room.add_argument('number', type=int)
pars_room.add_argument('level', type=str)
pars_room.add_argument('status', type=str)
pars_room.add_argument('price', type=int)

pars_staff = reqparse.RequestParser()
pars_staff.add_argument('name', type=str)
pars_staff.add_argument('passport_id', type=str)
pars_staff.add_argument('position', type=str)
pars_staff.add_argument('salary', type=int)

pars_tenants = reqparse.RequestParser()
pars_tenants.add_argument('name', type=str)
pars_tenants.add_argument('passport_id', type=str)
pars_tenants.add_argument('age', type=str)
pars_tenants.add_argument('sex', type=str)
pars_tenants.add_argument('address', type=str)
pars_tenants.add_argument('room_number', type=int)

pars_tenants_address = reqparse.RequestParser()
pars_tenants_address.add_argument('street', type=str)
pars_tenants_address.add_argument('city', type=str)
pars_tenants_address.add_argument('state', type=str)
pars_tenants_address.add_argument('zip', type=int)

