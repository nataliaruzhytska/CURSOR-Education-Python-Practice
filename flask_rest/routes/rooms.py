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

    def post(self):
        data = json.loads(request.data)
        new_room = Room(**data)
        db.session.add(new_room)
        db.session.commit()
        return "Successfully added a new room"

    def put(self, room_id):
        data = json.loads(request.data)
        room = Room.query.get(room_id)
        room.status = data.get("status")
        room.tenant_id = data.get("tenant_id")
        db.session.commit()
        return "Successfully updated the room"

    def delete(self):
        room = Room.query.get(pars_room.parse_args().get('room_id'))
        db.session.delete(room)
        db.session.commit()
        return "Successfully deleted the room"
