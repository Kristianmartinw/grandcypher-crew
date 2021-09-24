from flask import Blueprint
from app.models import Element

element_routes = Blueprint('elements', __name__)

@element_routes.route('/')
def elements():

    elements = Element.query.all()

    return {element.id:element.to_dict() for element in elements}
