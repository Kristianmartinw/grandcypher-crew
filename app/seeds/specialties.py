from app.models import db, Specialty


def seed_specialties():

    specialties = ['Sabre', 'Dagger', 'Spear', 'Axe', 'Staff', 'Gun', 'Melee', 'Bow', 'Harp', 'Katana' ]

    for specialty in specialties:
        new_specialty = Specialty(name=specialty)
        db.session.add(new_specialty)

    db.session.commit()


def undo_specialties():
    db.session.execute('TRUNCATE specialties RESTART IDENTITY CASCADE;')
    db.session.commit()
