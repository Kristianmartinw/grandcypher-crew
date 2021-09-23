from app.models import db, Archetype


def seed_archetypes():

    archetypes = ['Enmity', 'Stamina', 'Sustain', 'Ougi', 'Skill Damage', 'Otk', 'Multi' ]

    for archetype in archetypes:
        new_archetype = Archetype(name=archetype)
        db.session.add(new_archetype)

    db.session.commit()


def undo_archetypes():
    db.session.execute('TRUNCATE archetypes RESTART IDENTITY CASCADE;')
    db.session.commit()
