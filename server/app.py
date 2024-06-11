from flask import Flask, jsonify, request, abort
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance

app = Flask(__name__)

# Configuring SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Routes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    episodes_data = [episode.to_dict() for episode in episodes]
    return jsonify(episodes_data)
    
@app.route('/episodes/<int:episode_id>', methods=['GET'])
def get_episode(episode_id):
    episode = Episode.query.get_or_404(episode_id)
    appearances_data = [
        {
            "episode_id": appearance.episode_id,
            "guest": {
                "id": appearance.guest.id,
                "name": appearance.guest.name,
                "occupation": appearance.guest.occupation
            },
            "guest_id": appearance.guest_id,
            "id": appearance.id,
            "rating": appearance.rating
        }
        for appearance in episode.appearances
    ]
    episode_data = episode.to_dict()
    episode_data["appearances"] = appearances_data
    return jsonify(episode_data)

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        new_appearance = Appearance(
            episode_id=data['episode_id'],
            guest_id=data['guest_id'],
            rating=data['rating']
        )
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify(new_appearance.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/appearances/<int:id>', methods=['DELETE'])
def delete_appearance(id):
    appearance = Appearance.query.get_or_404(id)
    db.session.delete(appearance)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
