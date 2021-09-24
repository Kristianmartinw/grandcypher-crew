from flask import Blueprint
from app.models import Party

party_routes = Blueprint('partys', __name__)

@party_routes.route('/')
def partys():

    partys = Party.query.all()

    return {party.id:party.to_dict() for party in partys}
