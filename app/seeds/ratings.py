from app.models import db, Rating

def seed_ratings():

    rating1 = Rating(
        user_id=1,
        party_id=1,
        value=4
    )

    db.session.add(rating1)

    db.session.commit()

def undo_ratings():
    db.session.execute('TRUNCATE ratings RESTART IDENTITY CASCADE;')
    db.session.commit()
