from .db import db


class ChargeAttack(db.Model):
    __tablename__ = 'charge_attacks'

# columns
    id = db.Column(db.Integer, primary_key=True)
    charge_attack_url = db.Column(db.String)
    name = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "charge_attack_url": self.charge_attack_url,
            "name": self.name,
        }
