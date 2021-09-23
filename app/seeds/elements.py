from app.models import db, Element


def seed_elements():

    elements = ['Water', 'Fire', 'Wind', 'Earth', 'Light', 'Dark' ]

    for element in elements:
        new_element = Element(name=element)
        db.session.add(new_element)

    db.session.commit()


def undo_elements():
    db.session.execute('TRUNCATE elements RESTART IDENTITY CASCADE;')
    db.session.commit()
