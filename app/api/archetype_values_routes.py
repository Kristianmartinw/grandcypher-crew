from flask import Blueprint
from app.models import ArchetypeValue

archetype_value_routes = Blueprint('archetype_values', __name__)

@archetype_value_routes.route('/')
def archetype_values():

    archetype_values = ArchetypeValue.query.all()

    return {archetype_values.id:archetype_values.to_dict() for archetype_values in archetype_values}
