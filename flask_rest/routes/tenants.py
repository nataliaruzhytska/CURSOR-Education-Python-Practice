from flask import Blueprint
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
        all_tenants.append(Tenants(pars_tenants.parse_args().get('name'),
                                   pars_tenants.parse_args().get('passport_id'),
                                   pars_tenants.parse_args().get('age'),
                                   pars_tenants.parse_args().get('sex'),
                                   {'street': pars_tenants_address.parse_args().get('street'),
                                    'city': pars_tenants_address.parse_args().get('city'),
                                    'state': pars_tenants_address.parse_args().get('state'),
                                    'zip': pars_tenants_address.parse_args().get('zip')},
                                   pars_tenants.parse_args().get('room_number')))
        return all_tenants, 200

    @marshal_with(tenants_fields)
    def put(self, tenant_id):
        for tenant in all_tenants:
            if tenant.passport_id == tenant_id:
                tenant.room_number = pars_tenants.parse_args().get('room_number')
                return tenant, 200

    @marshal_with(tenants_fields)
    def delete(self):
        for tenant in all_tenants:
            if pars_tenants.parse_args().get('passport_id') == tenant.passport_id:
                all_tenants.remove(tenant)

                return all_tenants, 200
