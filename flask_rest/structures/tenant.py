from flask_restful import fields


class Tenants:

    def __init__(self, name, passport_id, age, sex, address, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.address = address
        self.room_number = room_number


address_fields = {'street': fields.String,
                  'city': fields.String,
                  'state': fields.String,
                  'zip': fields.Integer}

tenants_fields = {'name': fields.String,
                  'passport_id': fields.String,
                  'age': fields.String,
                  'sex': fields.String,
                  'address': fields.Nested(address_fields),
                  'room_number': fields.Integer}


all_tenants = [Tenants("Irina", "PL09876", 36, "F", {
                                                        "street": " Palladina",
                                                        "city": "Kyiv",
                                                        "state": "Ukraine",
                                                        "zip": 30225}, 123),
               Tenants("Nataliia", "KJ87654", 29, "F", {
                                                       "street": " Shevchenka",
                                                       "city": "Kyiv",
                                                       "state": "Ukraine",
                                                       "zip": 54554}, 436),
               Tenants("Ihor", "GH98653", 18, "M", {
                                                       "street": " Palladina",
                                                       "city": "Lviv",
                                                       "state": "Ukraine",
                                                       "zip": 86432}, 567)]
