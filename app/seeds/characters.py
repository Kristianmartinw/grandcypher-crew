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
    predator = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Predator/predator-url.png',
        name='Predator',
        max_hp=1100,
        max_atk=10500,
        element_id=6,
        race_id=1,
        specialty_id=7,
        archetype_id=1,
        charge_attack_id=2,
    )
    rei = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Rei/rei-url.png',
        name='Rei',
        max_hp=1000,
        max_atk=10000,
        element_id=6,
        race_id=4,
        specialty_id=5,
        archetype_id=7,
        charge_attack_id=3,
    )
    helel = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Helel/helel-url.png',
        name='Helel ben Shalem',
        max_hp=1270,
        max_atk=8880,
        element_id=6,
        race_id=6,
        specialty_id=3,
        archetype_id=3,
        charge_attack_id=4,
    )
    olivia = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Olivia/olivia-url.png',
        name='Olivia',
        max_hp=1480,
        max_atk=7800,
        element_id=6,
        race_id=5,
        specialty_id=1,
        archetype_id=8,
        charge_attack_id=5,
    )
    orchid = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Orchid/orchid-url.png',
        name='Orchid',
        max_hp=1950,
        max_atk=8850,
        element_id=6,
        race_id=6,
        specialty_id=7,
        archetype_id=2,
        charge_attack_id=6,
    )
    black_knight = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-BlackKnight/blackknight-url.png',
        name='Black Knight',
        max_hp=1780,
        max_atk=11850,
        element_id=6,
        race_id=1,
        specialty_id=1,
        archetype_id=1,
        charge_attack_id=7,
    )
    clarisse = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Clarisse/clarisse-url.png',
        name='Clarisse',
        max_hp=1214,
        max_atk=9130,
        element_id=6,
        race_id=1,
        specialty_id=5,
        archetype_id=3,
        charge_attack_id=8,
    )
    kolulu = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Kolulu/kolulu-url.png',
        name='Kolulu',
        max_hp=1190,
        max_atk=11100,
        element_id=6,
        race_id=1,
        specialty_id=3,
        archetype_id=1,
        charge_attack_id=9,
    )
    meg = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Meg/meg-url.png',
        name='Meg',
        max_hp=1080,
        max_atk=10600,
        element_id=6,
        race_id=1,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=10,
    )
    narmaya = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Narmaya/narmiya-url.png',
        name='Narmaya',
        max_hp=1330,
        max_atk=12200,
        element_id=6,
        race_id=2,
        specialty_id=10,
        archetype_id=6,
        charge_attack_id=11,
    )
    vikala = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Vikala/vikala-url.png',
        name='Vikala',
        max_hp=1750,
        max_atk=9000,
        element_id=6,
        race_id=1,
        specialty_id=7,
        archetype_id=4,
        charge_attack_id=13,
    )
    amira = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Amira/amira-url.png',
        name='Amira',
        max_hp=1960,
        max_atk=6750,
        element_id=6,
        race_id=6,
        specialty_id=7,
        archetype_id=3,
        charge_attack_id=14,
    )
    anthuria = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Anthuria/anthuria-url.png',
        name='Anthuria',
        max_hp=1480,
        max_atk=7000,
        element_id=6,
        race_id=3,
        specialty_id=7,
        archetype_id=3,
        charge_attack_id=15,
    )
    tabina = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Tabina/tabina-url.png',
        name='Tabina',
        max_hp=1245,
        max_atk=9775,
        element_id=6,
        race_id=1,
        specialty_id=8,
        archetype_id=5,
        charge_attack_id=16,
    )
    vaseraga = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Vaseraga/vaseraga-url.png',
        name='Vaseraga',
        max_hp=1890,
        max_atk=13170,
        element_id=6,
        race_id=2,
        specialty_id=4,
        archetype_id=1,
        charge_attack_id=17,
    )
    wulf_and_renie = Character(
        character_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Wulfandrenie/wulfandrenie-url.png',
        name='Wulf and Renie',
        max_hp=1480,
        max_atk=8600,
        element_id=6,
        race_id=6,
        specialty_id=7,
        archetype_id=6,
        charge_attack_id=18,
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

def undo_characters():
    db.session.execute('TRUNCATE characters RESTART IDENTITY CASCADE;')
    db.session.commit()
