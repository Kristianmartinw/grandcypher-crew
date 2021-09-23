from app.models import db, ArchetypeValue

def seed_archetype_values():

    zooey = ArchetypeValue(
        character_id=1,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )

    db.session.add(zooey)

    db.session.commit()

def undo_archetype_values():
    db.session.execute('TRUNCATE archetype_values RESTART IDENTITY CASCADE;')
    db.session.commit()
