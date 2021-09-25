from app.models import db, Element


def seed_elements():

    elements = [
        {'name': 'Water', 'element_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/elements/element-water.png'},
        {'name': 'Fire', 'element_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/elements/element-fire.png'},
        {'name': 'Wind', 'element_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/elements/element-wind.png'},
        {'name': 'Earth', 'element_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/elements/element-earth.png'},
        {'name': 'Light', 'element_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/elements/element-light.png'},
        {'name': 'Dark', 'element_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/elements/element-dark.png'},
        {'name': 'Wheel', 'element_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/elements/element-vulnerabilities.png'}
        ]

    for element in elements:
        new_element = Element(name=element['name'], element_url=element['element_url'])
        db.session.add(new_element)

    db.session.commit()


def undo_elements():
    db.session.execute('TRUNCATE elements RESTART IDENTITY CASCADE;')
    db.session.commit()
