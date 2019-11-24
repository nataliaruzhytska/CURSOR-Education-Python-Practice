from flask_restful import fields


class Staff:

    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary


staff_fields = {'name': fields.String,
                'passport_id': fields.String,
                'position': fields.String,
                'salary': fields.Integer}


all_staff = [Staff("Mariia", "GF56780", "director", 1250),
             Staff("Anna", "RS89780", "administrator", 750),
             Staff("Olga", "DF98765", "cleaning", 500)]
