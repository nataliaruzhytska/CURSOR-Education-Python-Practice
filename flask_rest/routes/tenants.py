import json

from flask import Blueprint, request, current_app
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

    @marshal_with(tenants_fields)
    def post(self):
        data = json.loads(request.data)
        try:
            room_id = data.pop('room_id')
            room = Room.query.get(room_id)
            data['rooms'] = room
        except KeyError:
            current_app.logger.info("Room was not added")
            try:
                new_tenant = Tenant(**data)
                db.session.add(new_tenant)
                db.session.commit()
                return new_tenant, f"Successfully added a new tenant {new_tenant}"
            except(ValueError, TypeError, KeyError):
                return Tenant.query.all(), "Error! New tenant was not created"

    @marshal_with(tenants_fields)
    def put(self, tenant_id):
        data = json.loads(request.data)
        tenant = Tenant.query.get(tenant_id)
        if tenant:
            try:
                tenant.city = data["city"]
                tenant.address = data["address"]
                db.session.commit()
                return tenant, f"Successfully updated the tenant {tenant.name}"
            except(ValueError, TypeError, KeyError):
                return tenant, f"Error! The tenant {tenant.name} was not updated"
        else:
            return Tenant.query.all(), "There is no tenant with this ID"

    @marshal_with(tenants_fields)
    def delete(self, tenant_id):
        tenant = Tenant.query.get(tenant_id)
        if tenant:
            try:
                db.session.delete(tenant)
                db.session.commit()
                return tenant, f"Successfully deleted the tenant {tenant.name}"
            except(ValueError, TypeError, KeyError):
                return tenant, f"Error! The tenant {tenant.name} was not deleted"
        else:
            return Tenant.query.all(), "There is no tenant with this ID"
