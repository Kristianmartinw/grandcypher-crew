from flask import Blueprint
from app.models import SupportSkill

support_skill_routes = Blueprint('support_skills', __name__)

@support_skill_routes.route('/')
def support_skills():

    support_skills = SupportSkill.query.all()

    return {support_skill.id:support_skill.to_dict() for support_skill in support_skills}
