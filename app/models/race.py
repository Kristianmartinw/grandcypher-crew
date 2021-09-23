from .db import db


class Race(db.Model):
    __tablename__ = 'races'

# columns
    id = db.Column(db.Integer, primary_key=True)
    race_url = db.Column(db.String)
    name = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "race_url": self.race_url,
            "name": self.name,
        }
