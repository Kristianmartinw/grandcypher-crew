from flask import Blueprint
from app.models import ChargeAttack

charge_attack_routes = Blueprint('charge_attacks', __name__)

@charge_attack_routes.route('/')
def charge_attacks():

    charge_attacks = ChargeAttack.query.all()

    return {charge_attack.id:charge_attack.to_dict() for charge_attack in charge_attacks}
