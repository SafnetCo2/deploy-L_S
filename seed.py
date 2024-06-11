import csv
from server import create_app
from server.models import db, Episode, Guest, Appearance

app = create_app()

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        with open('seed.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                year = row['YEAR']
                occupation = row['GoogleKnowlege_Occupation']
                show_date = row['Show']
                raw_guest_list = row['Raw_Guest_List']
                guest_names = [name.strip() for name in raw_guest_list.split(',')]

                episode = Episode.query.filter_by(date=show_date).first()
                if not episode:
                    episode = Episode(date=show_date, number=int(year))
                    db.session.add(episode)
                    db.session.commit()

                for guest_name in guest_names:
                    guest = Guest.query.filter_by(name=guest_name).first()
                    if not guest:
                        guest = Guest(name=guest_name, occupation=occupation)
                        db.session.add(guest)
                        db.session.commit()

                    appearance = Appearance(
                        episode_id=episode.id,
                        guest_id=guest.id,
                        rating=5  # Assuming a default rating of 5, you can modify this as needed
                    )
                    db.session.add(appearance)

            db.session.commit()

if __name__ == '__main__':
    seed_database()
