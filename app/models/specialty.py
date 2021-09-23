from .db import db


class Specialty(db.Model):
    __tablename__ = 'specialties'

 # columns
    id = db.Column(db.Integer, primary_key=True)
    specialty_url = db.Column(db.String)
    name = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "specialty_url": self.specialty_url,
            "name": self.name,
        }
