from app.models import db, SupportSkill


def seed_support_skills():

    zooey = SupportSkill(
        character_id=1,
        name='Envoy of Mediation',
    )

    db.session.add(zooey)

    db.session.commit()

def undo_support_skills():
    db.session.execute('TRUNCATE support_skills RESTART IDENTITY CASCADE;')
    db.session.commit()
