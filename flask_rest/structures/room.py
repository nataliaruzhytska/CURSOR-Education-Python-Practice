from flask_restful import fields


class Rooms:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


room_fields = {'number': fields.Integer,
               'level': fields.String,
               'status': fields.String,
               'price': fields.Integer}

all_rooms = [Rooms(123, "standart", "closed", 150),
             Rooms(246, "standart", "open", 175),
             Rooms(543, "lux", "open", 500)]
