from app.models import db, Skill


def seed_skills():

    zooey = ['Resolution', 'Conjunction', 'Thunder']

    for skills in zooey:
        new_skill = Skill(name=skills, character_id=1)
        db.session.add(new_skill)

    db.session.commit()

def undo_skills():
    db.session.execute('TRUNCATE skills RESTART IDENTITY CASCADE;')
    db.session.commit()
