from flask import Blueprint
from app.models import Specialty

specialty_routes = Blueprint('specialties', __name__)

@specialty_routes.route('/')
def specialties():

    specialties = Specialty.query.all()

    return {specialty.id:specialty.to_dict() for specialty in specialties}
