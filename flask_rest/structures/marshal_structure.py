from flask_restful import fields


room_fields = {'room_id': fields.Integer,
               'number': fields.Integer,
               'level': fields.String,
               'status': fields.String,
               'price': fields.Integer,
               'tenant_id': fields.Integer}


room_tenants = {'number': fields.Integer,
                'level': fields.String,
                'price': fields.Integer}


staff_fields = {'staff_id': fields.Integer,
                'name': fields.String,
                'passport_id': fields.String,
                'position': fields.String,
                'salary': fields.Integer,
                'rooms': fields.Nested(room_fields)}


tenants_fields = {'tenant_id': fields.Integer,
                  'name': fields.String,
                  'passport_id': fields.String,
                  'age': fields.Integer,
                  'sex': fields.String,
                  'city': fields.String,
                  'address': fields.String,
                  'rooms': fields.Nested(room_tenants)}
