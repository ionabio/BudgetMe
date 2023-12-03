
from flask import Blueprint, request
from services import index as services

routes = Blueprint('routes', __name__)

@routes.route('/transactions', methods=['GET'])
def get_transactions():
    return services.get_transactions()

@routes.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.get_json()
    return services.add_transaction(data)

@routes.route('/budget', methods=['GET'])
def get_budget():
    return services.get_budget()

@routes.route('/budget', methods=['POST'])
def set_budget():
    data = request.get_json()
    return services.set_budget(data)