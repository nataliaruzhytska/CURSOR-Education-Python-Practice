import json

from flask import request
from flask_restful import Resource, marshal_with

from db import db
from structures.marshal_structure import room_fields
from flask import Blueprint
from structures.model import Room
from structures.parsers import pars_room


rooms_bp = Blueprint('GetRooms', __name__)


class GetRooms(Resource):

    @marshal_with(room_fields)
    def get(self):
        if pars_room.parse_args().get('room_id'):
            data = Room.query.get(pars_room.parse_args().get('room_id'))
            return data
        return Room.query.all()

    @marshal_with(room_fields)
    def post(self):
        try:
            data = json.loads(request.data)
            new_room = Room(**data)
            db.session.add(new_room)
            db.session.commit()
            return new_room, f"Successfully added a new room {new_room.number}"
        except(ValueError, TypeError, KeyError):
            return Room.query.all(), "Error! New room was not created"

    @marshal_with(room_fields)
    def put(self, room_id):
        data = json.loads(request.data)
        room = Room.query.get(room_id)
        if room:
            try:
                room.status = data["status"]
                room.tenant_id = data["tenant_id"]
                db.session.commit()
                return room, "Successfully updated the room"
            except(ValueError, TypeError, KeyError):
                return room, "Error! The room was not updated"
        else:
            return Room.query.all(), "There is no room with this number"

    @marshal_with(room_fields)
    def delete(self, room_id):
        room = Room.query.get(room_id)
        if room:
            try:
                db.session.delete(room)
                db.session.commit()
                return Room.query.all(), f"Successfully deleted the room {room.number}"
            except(ValueError, TypeError, KeyError):
                return room, "Error! The room was not deleted"
        else:
            return Room.query.all(), "There is no room with this number"
