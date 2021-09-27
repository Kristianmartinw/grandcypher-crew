from app.models import db, ChargeAttack

def seed_charge_attacks():

    ca_list = [
        'Gamma Ray',
        'Thousand Claws',
        'Clairvoyant Bliss',
        'Chaos Legion',
        'Dark Fallen Sword',
        'Verdict Bringer',
        'Sword of Delusion',
        'Alkahest Sphere',
        'Stone Breaker',
        'Heavy Sharklone',
        'Dawnfly Dance II',
        'Freeflutter Dance II',
        'Gilded Heaven Strike',
        'Valley of the Damned',
        'Passione Perpetua',
        'Sa\'ada Barq',
        'Carnage Moon',
        'Hollow Blast'
         ]

    for charge_attacks in ca_list:
        new_charge_attack = ChargeAttack(name=charge_attacks, charge_attack_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/charge-attacks-and-support-skills/charge-attack.png')
        db.session.add(new_charge_attack)

    db.session.commit()

def undo_charge_attacks():
    db.session.execute('TRUNCATE charge_attacks RESTART IDENTITY CASCADE;')
    db.session.commit()
