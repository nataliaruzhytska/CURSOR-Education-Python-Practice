import json

from flask import Blueprint, request
from flask_restful import Resource, marshal_with

from structures.parsers import pars_room
from structures.room import Rooms, all_rooms, room_fields

rooms_bp = Blueprint('GetRooms', __name__)


class GetRooms(Resource):

    @marshal_with(room_fields)
    def get(self):
        for room in all_rooms:
            if pars_room.parse_args().get('number') == room.number:
                return room
        if pars_room.parse_args().get('status'):
            f_rooms = [room for room in all_rooms if pars_room.parse_args().get('status') == room.status]
            return f_rooms
        else:
            return all_rooms

    @marshal_with(room_fields)
    def post(self):
        data = json.loads(request.data)
        new_room = Rooms(**data)
        all_rooms.append(new_room)
        return all_rooms, 200

    @marshal_with(room_fields)
    def put(self, room_id):
        for room in all_rooms:
            if room.number == room_id:
                room.status = pars_room.parse_args().get('status')
                return room, 200
            else:
                return "There is no room with this number", 404

    @marshal_with(room_fields)
    def delete(self):
        for room in all_rooms:
            if pars_room.parse_args().get('number') == room.number:
                all_rooms.remove(room)
                return all_rooms, 200