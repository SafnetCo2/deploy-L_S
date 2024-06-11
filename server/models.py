from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class Episode(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.String, nullable=False)
#     number = db.Column(db.Integer, nullable=False)
#     appearances = db.relationship('Appearance', backref='episode', cascade='all, delete-orphan')

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "date": self.date,
#             "number": self.number,
#             "appearances": [appearance.to_dict() for appearance in self.appearances]
#         }
class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    appearances = db.relationship('Appearance', backref='episode', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            
            "id": self.id,
            "date": self.date,
            "number": self.id  # Ensure number is the same as id
        }

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "occupation": self.occupation}

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    guest = db.relationship('Guest')

    def to_dict(self):
        return {"id": self.id, "episode_id": self.episode_id, "guest_id": self.guest_id, "rating": self.rating, "guest": self.guest.to_dict()}
