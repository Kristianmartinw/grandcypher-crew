from app.models import db, Race


def seed_races():

    races = [
        {'name': 'Human', 'race_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/races/race-human.png'},
        {'name': 'Draph', 'race_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/races/race-draph.png'},
        {'name': 'Erune', 'race_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/races/race-erune.png'},
        {'name': 'Harvin', 'race_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/races/race-harvin.png'},
        {'name': 'Primal', 'race_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/races/race-primal.png'},
        {'name': 'Unknown', 'race_url': 'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/races/race-unknown.png'}
        ]

    for race in races:
        new_race = Race(name=race['name'], race_url=race['race_url'])
        db.session.add(new_race)

    db.session.commit()


def undo_races():
    db.session.execute('TRUNCATE races RESTART IDENTITY CASCADE;')
    db.session.commit()
