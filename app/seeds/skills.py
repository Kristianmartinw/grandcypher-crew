from app.models import db, Skill


def seed_skills():

    zooey = [
    {'name': 'Resolution', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Zooey/skill-resolution.png' },
    {'name': 'Conjunction', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Zooey/skill-conjunction.png'},
    {'name': 'Thunder', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Zooey/skill-thunder.png'}
    ]

    for skills in zooey:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=1)
        db.session.add(new_skill)

    db.session.commit()

def undo_skills():
    db.session.execute('TRUNCATE skills RESTART IDENTITY CASCADE;')
    db.session.commit()
