from .db import db
from .character_party_joins import character_party_joins


class Character(db.Model):
    __tablename__ = 'characters'

    # columns
    id = db.Column(db.Integer, primary_key=True)
    character_url = db.Column(db.String)
    name = db.Column(db.String(100))
    max_hp = db.Column(db.Integer)
    max_atk = db.Column(db.Integer)
    element_id = db.Column(db.Integer, db.ForeignKey("elements.id"))
    race_id = db.Column(db.Integer, db.ForeignKey("races.id"))
    specialty_id = db.Column(db.Integer, db.ForeignKey("specialties.id"))
    archetype_id = db.Column(db.Integer, db.ForeignKey("archetypes.id"))
    charge_attack_id = db.Column(db.Integer, db.ForeignKey("charge_attacks.id"))

    archetype_value=db.relationship('ArchetypeValue')
    archetype=db.relationship('Archetype', back_populates='characters')
    skills=db.relationship('Skill')
    parties=db.relationship('Party', secondary=character_party_joins, back_populates='characters')

    def to_dict(self):
        return {
            "archetype_values": {
                "enmity_value": self.archetype_value.enmity_value,
                "stamina_value": self.archetype_value.stamina_value,
                "sustain_value": self.archetype_value.sustain_value,
                "ougi_value": self.archetype_value.ougi_value,
                "skill_damage_value": self.archetype_value.skill_damage_value,
                "otk_value": self.archetype_value.otk_value,
                "multi_value": self.archetype_value.multi_value
            },
            "id": self.id,
            "character_url": self.character_url,
            "name": self.name,
            "max_hp": self.max_hp,
            "max_atk": self.max_atk,
            "element_id": self.element_id,
            "race_id": self.race_id,
            "specialty_id": self.specialty_id,
            "archetype_id": self.archetype_id,
            "charge_attack_id": self.charge_attack_id,
        }
