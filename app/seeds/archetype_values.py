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
    predator = ArchetypeValue(
        character_id=2,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    rei = ArchetypeValue(
        character_id=3,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    helel = ArchetypeValue(
        character_id=4,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    olivia = ArchetypeValue(
        character_id=5,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    orchid = ArchetypeValue(
        character_id=6,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    black_knight = ArchetypeValue(
        character_id=7,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    clarisse = ArchetypeValue(
        character_id=8,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    kolulu = ArchetypeValue(
        character_id=9,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    meg = ArchetypeValue(
        character_id=10,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    narmaya = ArchetypeValue(
        character_id=11,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    vikala = ArchetypeValue(
        character_id=12,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    amira = ArchetypeValue(
        character_id=13,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    anthuria = ArchetypeValue(
        character_id=14,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    tabina = ArchetypeValue(
        character_id=15,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    vaseraga = ArchetypeValue(
        character_id=16,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )
    wulf_and_renie = ArchetypeValue(
        character_id=17,
        enmity_value=100,
        stamina_value=0,
        sustain_value=0,
        ougi_value=0,
        skill_damage_value=0,
        otk_value=100,
        multi_value=0,
    )

    db.session.add(zooey)
    db.session.add(predator)
    db.session.add(rei)
    db.session.add(helel)
    db.session.add(olivia)
    db.session.add(orchid)
    db.session.add(black_knight)
    db.session.add(clarisse)
    db.session.add(kolulu)
    db.session.add(meg)
    db.session.add(narmaya)
    db.session.add(vikala)
    db.session.add(amira)
    db.session.add(anthuria)
    db.session.add(tabina)
    db.session.add(vaseraga)
    db.session.add(wulf_and_renie)

    db.session.commit()

def undo_archetype_values():
    db.session.execute('TRUNCATE archetype_values RESTART IDENTITY CASCADE;')
    db.session.commit()
