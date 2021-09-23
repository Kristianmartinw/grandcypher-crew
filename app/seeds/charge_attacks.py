from app.models import db, ChargeAttack

def seed_charge_attacks():

    ca_list = ['Gamma Ray']

    for charge_attacks in ca_list:
        new_charge_attack = ChargeAttack(name=charge_attacks, charge_attack_url='https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/charge-attacks-and-support-skills/charge-attack.png')
        db.session.add(new_charge_attack)

    db.session.commit()

def undo_charge_attacks():
    db.session.execute('TRUNCATE charge_attacks RESTART IDENTITY CASCADE;')
    db.session.commit()
