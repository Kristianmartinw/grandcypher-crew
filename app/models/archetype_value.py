from .db import db


class ArchetypeValue(db.Model):
    __tablename__ = 'archetype_values'

    # columns
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    enmity_value = db.Column(db.Integer)
    stamina_value = db.Column(db.Integer)
    sustain_value = db.Column(db.Integer)
    ougi_value = db.Column(db.Integer)
    skill_damage_value = db.Column(db.Integer)
    otk_value = db.Column(db.Integer)
    multi_value = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "character_id": self.character_id,
            "enmity_value": self.enmity_value,
            "stamina_value": self.stamina_value,
            "sustain_value": self.sustain_value,
            "ougi_value": self.ougi_value,
            "skill_damage_value": self.skill_damage_value,
            "otk_value": self.otk_value,
            "multi_value": self.multi_value
        }
