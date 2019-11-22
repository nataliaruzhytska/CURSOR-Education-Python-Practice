import json

from flask import Blueprint, request
from flask_restful import Resource, marshal_with

from structures.parsers import pars_tenants, pars_tenants_address
from structures.tenant import Tenants, all_tenants, tenants_fields


tenants_bp = Blueprint('GetTenants', __name__)


class GetTenants(Resource):

    @marshal_with(tenants_fields)
    def get(self):
        for tenant in all_tenants:
            if pars_tenants.parse_args().get('passport_id') == tenant.passport_id:
                return tenant
        else:
            return all_tenants

    @marshal_with(tenants_fields)
    def post(self):
        data = json.loads(request.data)
        new_tenant = Tenants(**data)
        all_tenants.append(new_tenant)
        return all_tenants, 200

    @marshal_with(tenants_fields)
    def put(self, tenant_id):
        for tenant in all_tenants:
            if tenant.passport_id == tenant_id:
                tenant.room_number = pars_tenants.parse_args().get('room_number')
                return tenant, 200
            else:
                return "No information about the tenant with this passport id", 404

    @marshal_with(tenants_fields)
    def delete(self):
        for tenant in all_tenants:
            if pars_tenants.parse_args().get('passport_id') == tenant.passport_id:
                all_tenants.remove(tenant)
                return all_tenants, 200
