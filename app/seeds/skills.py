from app.models import db, Skill


def seed_skills():

    zooey = [
    {'name': 'Resolution', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Zooey/skill-resolution.png' },
    {'name': 'Conjunction', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Zooey/skill-conjunction.png'},
    {'name': 'Thunder', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Zooey/skill-thunder.png'}
    ]
    predator = [
    {'name': 'Assault Blow', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Predator/skill-assaultblow.png' },
    {'name': 'Creeping Shadow', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Predator/skill-creepingshadow.png'},
    {'name': 'Laughing Phantom', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Predator/skill-laughingphantom.png'}
    ]
    rei = [
    {'name': 'Alaya-Vijnana', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Rei/skill-alayavijnana.png' },
    {'name': 'Moksha', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Rei/skill-moksha.png'},
    {'name': 'Cold Stare', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Rei/skill-coldstare.png'},
    {'name': 'Ama no Sakate', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Rei/skill-amanosakate.png'}
    ]
    helel = [
    {'name': 'Abacab', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Helel/skill-abacab.png' },
    {'name': 'Invisible Touch', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Helel/skill-abilitytouch.png'},
    {'name': 'Los Endos', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Helel/skill-losendos.png'},
    ]
    olivia = [
    {'name': 'Sterling Sea', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Olivia/skill-sterlingsea.png' },
    {'name': 'Peccatum Mortale', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Olivia/skill-peccatummortale.png'},
    {'name': 'Nevermore', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Olivia/skill-nevermore.png'},
    ]
    orchid = [
    {'name': 'Puppet Strings', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Orchid/skill-puppetstrings.png' },
    {'name': 'Ancestral Aegis', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Orchid/skill-barrier.png'},
    {'name': 'Oblivion', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Orchid/skill-oblivion%2B.png'},
    ]
    black_knight = [
    {'name': 'Quadspell', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-BlackKnight/skill-quadspell.png' },
    {'name': 'Onyx Drain', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-BlackKnight/skill-onyxdrainpng.png'},
    {'name': 'Acumen', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-BlackKnight/skill-acumen.png'},
    {'name': 'Protector\'s Sword', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-BlackKnight/skill-protectorssword.png'}
    ]
    clarisse = [
    {'name': 'Heartfelt', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Clarisse/skill-heartfelt.png' },
    {'name': 'Sweet Entropy', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Clarisse/skill-sweetentropy.png'},
    {'name': 'Atomic Acceleration', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Clarisse/skill-atomicacceleration.png'},
    ]
    kolulu = [
    {'name': 'Girl of Steel', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Kolulu/skill-cover.png' },
    {'name': 'Tallyho', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Kolulu/skill-tallyho.png'},
    {'name': 'Still Alive', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Kolulu/skill-stillalive.png'},
    ]
    meg = [
    {'name': 'Sharklone Assault', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Meg/skill-sharkloneassault.png' },
    {'name': 'Shark in Open Water', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Meg/skill-sharkinopenwater.png'},
    {'name': 'Calamity Rejection', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Meg/skill-calamityrejection.png'},
    ]
    narmaya = [
    {'name': 'Butterfly Effect', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Narmaya/skill-butterfly.png' },
    {'name': 'Transient', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Narmaya/skill-transient.png'},
    {'name': 'Kyokasuigetsu', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Narmaya/skill-kyogasuigetsu.png'},
    {'name': 'Glasswing Waltz', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Narmaya/skill-glasswingwaltz.png'}
    ]
    vikala = [
    {'name': 'Ring the Dormouse', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Vikala/skill-ringthedormouse.png' },
    {'name': 'Dazzling Dreams', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Vikala/skill-dazzlingdreams.png'},
    {'name': 'Fantasy Festival', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Vikala/skill-fantasyfestival.png'},
    ]
    amira = [
    {'name': 'Summer\'s End', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Amira/skill-summersend.png' },
    {'name': 'Radiant Heart', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Amira/skill-radiantheart.png'},
    {'name': 'Maximum Overload', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Amira/skill-maximumoverload.png'},
    ]
    anthuria = [
    {'name': 'Bonfire Dance', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Anthuria/skill-bonfiredance.png' },
    {'name': 'Flowering Lily', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Anthuria/skill-floweringlily.png'},
    {'name': 'Setting the Tempo', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Anthuria/skill-settingthetempo.png'},
    ]
    tabina = [
    {'name': 'Shams Al-Saif', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Tabina/skill-shamsalsaif.png' },
    {'name': 'Al-Mawj Takil', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Tabina/skill-almawjtakil.png'},
    {'name': 'Hubu Al-Raqs', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Tabina/skill-hubualraqs.png'},
    ]
    vaseraga = [
    {'name': 'Great Scythe Grynoth', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Vaseraga/skill-greatscythegrynoth.png' },
    {'name': 'Instinction', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Vaseraga/skill-instinction%2B.png'},
    {'name': 'Forgotten Tales', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Vaseraga/skill-forgottentales%2B.png'},
    ]
    wulf_and_renie = [
    {'name': 'Herz aus Eisen', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Wulfandrenie/skill-herzauseisen.png' },
    {'name': 'Renie\'s Tears', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Wulfandrenie/skill-reniestears.png'},
    {'name': 'Rufen', 'skill_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/skills/Dark/D-Wulfandrenie/skill-rufen.png'},
    ]

    for skills in zooey:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=1)
        db.session.add(new_skill)

    for skills in predator:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=2)
        db.session.add(new_skill)

    for skills in rei:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=3)
        db.session.add(new_skill)

    for skills in helel:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=4)
        db.session.add(new_skill)

    for skills in olivia:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=5)
        db.session.add(new_skill)

    for skills in orchid:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=6)
        db.session.add(new_skill)

    for skills in black_knight:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=7)
        db.session.add(new_skill)

    for skills in clarisse:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=8)
        db.session.add(new_skill)

    for skills in kolulu:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=9)
        db.session.add(new_skill)

    for skills in meg:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=10)
        db.session.add(new_skill)

    for skills in narmaya:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=11)
        db.session.add(new_skill)

    for skills in vikala:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=12)
        db.session.add(new_skill)

    for skills in amira:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=13)
        db.session.add(new_skill)

    for skills in anthuria:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=14)
        db.session.add(new_skill)

    for skills in tabina:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=15)
        db.session.add(new_skill)

    for skills in vaseraga:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=16)
        db.session.add(new_skill)

    for skills in wulf_and_renie:
        new_skill = Skill(name=skills['name'], skill_url=skills['skill_url'], character_id=17)
        db.session.add(new_skill)

    db.session.commit()

def undo_skills():
    db.session.execute('TRUNCATE skills RESTART IDENTITY CASCADE;')
    db.session.commit()
