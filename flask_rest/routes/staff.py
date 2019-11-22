import json

from flask import Blueprint, request
from flask_restful import Resource, marshal_with

from structures.parsers import pars_staff
from structures.staff_s import Staff, all_staff, staff_fields


staff_bp = Blueprint('GetStaff', __name__)


class GetStaff(Resource):

    @marshal_with(staff_fields)
    def get(self):
        for staff in all_staff:
            if pars_staff.parse_args().get('passport_id') == staff.passport_id:
                return staff
        if pars_staff.parse_args().get('position'):
            f_staff = [staff for staff in all_staff if pars_staff.parse_args().get('position') == staff.position]
            return f_staff
        else:
            return all_staff

    @marshal_with(staff_fields)
    def post(self):
        data = json.loads(request.data)
        new_staff = Staff(**data)
        all_staff.append(new_staff)
        return all_staff, 200

    @marshal_with(staff_fields)
    def put(self, staff_id):
        for staff in all_staff:
            if staff.passport_id == staff_id:
                staff.position = pars_staff.parse_args().get('position')
                staff.salary = pars_staff.parse_args().get('salary')
                return staff, 200
            else:
                return "No information about the employee with this passport id", 404

    @marshal_with(staff_fields)
    def delete(self):
        for staff in all_staff:
            if pars_staff.parse_args().get('passport_id') == staff.passport_id:
                all_staff.remove(staff)
                return all_staff, 200
