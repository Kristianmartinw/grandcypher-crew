from app.models import db, Character

def seed_characters():

    zooey = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Zooey/zooey-url.png',
        name='Zooey',
        max_hp=1180,
        max_atk=9200,
        element_id=6,
        race_id=5,
        specialty_id=1,
        archetype_id=1,
        charge_attack_id=1,
    )

    db.session.add(zooey)

    db.session.commit()

def undo_characters():
    db.session.execute('TRUNCATE characters RESTART IDENTITY CASCADE;')
    db.session.commit()
