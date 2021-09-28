from flask import Blueprint, request
from app.models import Party, Character, character_party_joins,  db

party_routes = Blueprint('parties', __name__)

@party_routes.route('/')
def parties():
    parties = Party.query.all()
    return {party.id:party.to_dict() for party in parties}

@party_routes.route('/', methods=["POST"])
def create_party():
    data = request.get_json()
    new_party = Party(
        name=data['name'],
        owner_id=data['owner_id'],
    )
    db.session.add(new_party)
    db.session.commit()
    return new_party.to_dict()

@party_routes.route('/<int:party_id>/', methods=["PUT"])
def edit_party(party_id):
    data = request.get_json()
    party = Party.query.get(party_id)
    if party:
        party.name = data['name'],
        db.session.commit()
        return party.to_dict()
    return {"Error": "Party not found"}

@party_routes.route('/<int:party_id>/', methods=["DELETE"])
def delete_party(party_id):
    party = Party.query.get(party_id)
    if party:
        db.session.delete(party)
        db.session.commit()
        return {"Success": "Party deleted"}
    return {"Error": "Party failed to delete"}

@party_routes.route('/<int:party_id>/add', methods = ['POST'])
def add_character(party_id):
    data = request.get_json()

    character_id = data['character_id']

    db.session.execute(character_party_joins.insert().values(party_id = party_id, character_id = character_id))

    db.session.commit()

    party = Party.query.get(int(party_id))

    return party.to_dict()

@party_routes.route('/<int:party_id>/characters/<int:character_id>', methods = ['DELETE'])
def remove_character(party_id, character_id):
    db.session.execute(character_party_joins.delete().where(character_party_joins.c.party_id == +party_id).where(character_party_joins.c.character_id == +character_id))

    db.session.commit()

    party = Party.query.get(int(party_id))

    return party.to_dict()
