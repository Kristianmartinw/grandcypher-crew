from flask import Blueprint
from app.models import Archetype

archetype_routes = Blueprint('archetypes', __name__)

@archetype_routes.route('/')
def archetypes():

    archetypes = Archetype.query.all()

    return {archetype.id:archetype.to_dict() for archetype in archetypes}
