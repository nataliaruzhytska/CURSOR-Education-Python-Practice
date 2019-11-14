import json

from flask import Blueprint, request
from flask_restful import Resource, marshal_with

from db import db
from structures.marshal_structure import staff_fields
from structures.model import Staff, Room
from structures.parsers import pars_staff, staff_room_parser

staff_bp = Blueprint('GetStaff', __name__)


class GetStaff(Resource):

    @marshal_with(staff_fields)
    def get(self):
        if pars_staff.parse_args().get('staff_id'):
            data = Staff.query.get(pars_staff.parse_args().get('staff_id'))
            return data
        return Staff.query.all()

    def post(self):
        data = json.loads(request.data)
        new_staff = Staff(**data)
        db.session.add(new_staff)
        db.session.commit()
        return "Successfully added a new staff"

    def put(self, staff_id):
        data = json.loads(request.data)
        staff = Staff.query.get(staff_id)
        staff.position = data.get("position")
        staff.salary = data.get("salary")
        db.session.commit()
        return "Successfully updated the staff"

    def delete(self):
        staff = Staff.query.get(pars_staff.parse_args().get('staff_id'))
        db.session.delete(staff)
        db.session.commit()
        return "Successfully deleted the staff"


class StaffRoom(Resource):
    def post(self):
        data = json.loads(request.data)
        staff_name = data.get('staff_name')
        room_number = data.get('room_number')
        staff = Staff.query.filter_by(name=staff_name).first()
        room = Room.query.filter_by(number=room_number).first()
        staff.rooms.append(room)
        db.session.commit()
        return f"Successfully added {room.number} to {staff.name}"

    @marshal_with(staff_fields)
    def get(self):
        args = staff_room_parser.parse_args(strict=True)
        room = Room.query.filter_by(number=args.get('number')).first()
        return room.staff
