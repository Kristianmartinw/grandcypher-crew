from flask import Blueprint
from app.models import Character

character_routes = Blueprint('characters', __name__)

@character_routes.route('/')
def characters():

    characters = Character.query.all()

    return {character.id:character.to_dict() for character in characters}
