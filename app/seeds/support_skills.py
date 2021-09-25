from app.models import db, SupportSkill


def seed_support_skills():

    zooey = SupportSkill(
        character_id=1,
        name='Envoy of Mediation',
        support_skill_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/charge-attacks-and-support-skills/support-skill.png'
    )

    db.session.add(zooey)

    db.session.commit()

def undo_support_skills():
    db.session.execute('TRUNCATE support_skills RESTART IDENTITY CASCADE;')
    db.session.commit()
