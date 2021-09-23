from app.models import db, Party

def seed_parties():

    party1 = Party(
        name='Dark Enmity',
        owner_id=1
    )

    db.session.add(party1)

    db.session.commit()

def undo_parties():
    db.session.execute('TRUNCATE parties RESTART IDENTITY CASCADE;')
    db.session.commit()
