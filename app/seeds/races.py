from app.models import db, Race


def seed_races():

    races = ['Human', 'Draph', 'Erune', 'Harvin', 'Primal', 'Unknown']

    for race in races:
        new_race = Race(name=race)
        db.session.add(new_race)

    db.session.commit()


def undo_races():
    db.session.execute('TRUNCATE races RESTART IDENTITY CASCADE;')
    db.session.commit()
