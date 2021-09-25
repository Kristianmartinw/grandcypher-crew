from app.models import db, Specialty


def seed_specialties():

    specialties = [
        {'name': 'Sabre', 'specialty_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/specialties/specialty-sabre.png'},
        {'name': 'Dagger', 'specialty_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/specialties/specialty-dagger.png'},
        {'name': 'Spear', 'specialty_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/specialties/specialty-spear.png'},
        {'name': 'Axe', 'specialty_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/specialties/specialty-axe.png'},
        {'name': 'Staff', 'specialty_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/specialties/specialty-staff.png'},
        {'name': 'Gun', 'specialty_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/specialties/specialty-gun.png'},
        {'name': 'Melee', 'specialty_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/specialties/specialty-melee.png'},
        {'name': 'Bow', 'specialty_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/specialties/specialty-bow.png'},
        {'name': 'Harp', 'specialty_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/specialties/specialty-harp.png'},
        {'name': 'Katana', 'specialty_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/specialties/specialty-katana.png'}
        ]

    for specialty in specialties:
        new_specialty = Specialty(name=specialty['name'], specialty_url=specialty['specialty_url'])
        db.session.add(new_specialty)

    db.session.commit()


def undo_specialties():
    db.session.execute('TRUNCATE specialties RESTART IDENTITY CASCADE;')
    db.session.commit()
