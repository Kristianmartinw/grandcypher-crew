from app.models import db, character_party_joins

def seed_character_party_joins():

    db.session.execute(character_party_joins.insert().values(character_id=1, party_id=1))

    db.session.commit()

def undo_character_party_joins():
    db.session.execute('TRUNCATE character_party_joins RESTART IDENTITY CASCADE;')
    db.session.commit()
