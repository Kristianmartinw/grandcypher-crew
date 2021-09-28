from flask import Blueprint, request
from flask_login import login_required
from app.models import db, Party, Rating


rating_routes = Blueprint('ratings', __name__)

@rating_routes.route('/', methods=['POST'])
@login_required
def create_rating():
    data = request.get_json()
    party_id = data['party_id']
    user_id = data['user_id']
    value = data['value']

    new_rating = Rating(party_id=party_id, user_id=user_id, value=value)

    db.session.add(new_rating)
    db.session.commit()
    party = Party.query.get(party_id)
    return party.to_dict()

@rating_routes.route('/<int:id>/', methods=['PUT'])
@login_required
def edit_rating(id):
    value = request.get_json(['value'])
    rating = Rating.query.get(id)
    rating.value = value
    db.session.commit()
    party = Party.query.get(rating.party_id)
    return party.to_dict()

@rating_routes.route('/<int:id>/', methods={'DELETE'})
@login_required
def delete_rating(id):
    rating = Rating.query.get(id)
    party_id = rating.party_id
    db.session.delete(rating)
    db.session.commit()
    party = Party.query.get(party_id)
    return party.to_dict()
