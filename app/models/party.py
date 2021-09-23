from .db import db
from .character_party_joins import character_party_joins


class Party(db.Model):
    __tablename__ = 'parties'

    # columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    characters=db.relationship('Character', secondary=character_party_joins, back_populates='parties')

    def to_dict(self):
        return {
            "characters": [character.to_dict() for character in self.characters],
            "id": self.id,
            "name": self.name,
            "owner_id": self.owner_id,
        }
