from flask import Blueprint
from app.models import Skill

skill_routes = Blueprint('skills', __name__)

@skill_routes.route('/')
def skills():

    skills = Skill.query.all()

    return {skill.id:skill.to_dict() for skill in skills}
