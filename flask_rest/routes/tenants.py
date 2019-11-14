import json

from flask import Blueprint, request, jsonify, current_app
from flask_restful import Resource, marshal_with

from db import db
from structures.marshal_structure import tenants_fields
from structures.model import Tenant, Room
from structures.parsers import pars_tenants


tenants_bp = Blueprint('GetTenants', __name__)


class GetTenants(Resource):

    @marshal_with(tenants_fields)
    def get(self):
        if pars_tenants.parse_args().get('tenant_id'):
            data = Tenant.query.get(pars_tenants.parse_args().get('tenant_id'))
            return data
        return Tenant.query.all()

    def post(self):
        data = json.loads(request.data)
        try:
            room_id = data.pop('room_id')
            room = Room.query.get(room_id)
            data['rooms'] = room
        except KeyError:
            current_app.logger.info("Room was not added")
        new_tenant = Tenant(**data)
        db.session.add(new_tenant)
        db.session.commit()
        return "Successfully added a new tenant"

    def put(self, tenant_id):
        data = json.loads(request.data)
        tenant = Tenant.query.get(tenant_id)
        tenant.city = data.get("city")
        tenant.street = data.get("street")
        tenant.house = data.get("house")
        db.session.commit()
        return "Successfully updated the tenant"

    def delete(self):
        tenant = Tenant.query.get(pars_tenants.parse_args().get('tenant_id'))
        db.session.delete(tenant)
        db.session.commit()
        return "Successfully deleted the tenant"
