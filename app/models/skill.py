from .db import db


class Skill(db.Model):
    __tablename__ = 'skills'

# columns
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"))
    skill_url = db.Column(db.String)
    name = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "skill_url": self.skill_url,
            "name": self.name,
        }
