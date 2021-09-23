from .db import db


class Archetype(db.Model):
    __tablename__ = 'archetypes'

    # columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    characters=db.relationship('Character', back_populates='archetype')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
