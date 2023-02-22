from flask import request
from flask_restx import abort, Namespace, Resource

from implemented import user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthRegisterView(Resource):
    def post(self):
        data = request.json
        return user_service.create(data)

