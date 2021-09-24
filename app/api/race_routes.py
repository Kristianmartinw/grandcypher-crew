from flask import Blueprint
from app.models import Race

race_routes = Blueprint('races', __name__)

@race_routes.route('/')
def races():

    races = Race.query.all()

    return {race.id:race.to_dict() for race in races}
