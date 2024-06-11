from flask import jsonify, request
from . import create_app, db
from server.models import db, Episode, Guest, Appearance
# define routes here


app = create_app()

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

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

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify(episode.to_dict())

@app.route('/guests/<int:id>', methods=['GET'])
def get_guest(id):
    guest = Guest.query.get_or_404(id)
    return jsonify(guest.to_dict())
