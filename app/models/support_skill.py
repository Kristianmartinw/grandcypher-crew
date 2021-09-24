from .db import db


class SupportSkill(db.Model):
    __tablename__ = 'support_skills'

# columns
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"))
    support_skill_url = db.Column(db.String)
    name = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "support_skill_url": self.support_skill_url,
            "name": self.name,
        }
