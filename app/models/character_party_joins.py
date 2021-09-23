from .db import db

character_party_joins = db.Table(
    "character_party_joins",
    db.Column('id', db.Integer, primary_key=True),
    db.Column(
        'character_id', db.Integer, db.ForeignKey("characters.id")
    ),
    db.Column(
        'party_id', db.Integer, db.ForeignKey('parties.id')
    )
)
