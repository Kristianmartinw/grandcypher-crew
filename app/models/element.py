from .db import db


class Element(db.Model):
    __tablename__ = 'elements'

# columns
    id = db.Column(db.Integer, primary_key=True)
    element_url = db.Column(db.String)
    name = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "element_url": self.element_url,
            "name": self.name,
        }
