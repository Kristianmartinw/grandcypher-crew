from .db import db
from .character_party_joins import character_party_joins

def sort_by_id(e):
    return e['id']

class Party(db.Model):
    __tablename__ = 'parties'

    # columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    characters=db.relationship('Character', secondary=character_party_joins, back_populates='parties')
    ratings = db.relationship('Rating', cascade='all, delete-orphan')

    def to_dict(self):
        characters = [character.to_dict() for character in self.characters]
        characters.sort(key=sort_by_id)
        ratings =[{
            "id": rating.id,
            "userId": rating.user_id,
            "value": rating.value
        } for rating in self.ratings]
        return {
            "characters": characters,
            "id": self.id,
            "name": self.name,
            "owner_id": self.owner_id,
            "ratings": ratings
        }
