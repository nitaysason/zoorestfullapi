from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zoo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User entity model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    zoo_entities = db.relationship('ZooEntity', backref='user', lazy=True)

# Zoo entity model
class ZooEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    

# Create tables
with app.app_context():
    db.create_all()

# Routes

# Zoo Routes

@app.route('/zoo', methods=['GET'])
def get_all_entities():
    with app.app_context():
        entities = ZooEntity.query.all()
        result = [
            {"id": entity.id, "color": entity.color, "age": entity.age, "image": entity.image, "user_id": entity.user_id}
            for entity in entities
        ]
    return jsonify(result)

@app.route('/zoo/<int:entity_id>', methods=['GET'])
def get_entity(entity_id):
    with app.app_context():
        entity = ZooEntity.query.get(entity_id)
        if entity:
            result = {"id": entity.id, "color": entity.color, "age": entity.age, "image": entity.image, "user_id": entity.user_id}
            return jsonify(result)
        else:
            return jsonify({"message": "Entity not found"}), 404

from werkzeug.utils import secure_filename
import os

# Specify the folder where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/zoo', methods=['POST'])
def add_entity():
    data = request.form  # Access form data
    file = request.files['image']  # Access the uploaded file
    if 'image' in request.files and file.filename != '':
        # Save the file with a secure filename
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        with app.app_context():
            new_entity = ZooEntity(
                color=data['color'],
                age=data['age'],
                image=filename,  # Save the file name in the database
                user_id=data['user_id']
            )
            db.session.add(new_entity)
            db.session.commit()

        return jsonify({"message": "Entity added successfully"}), 201
    else:
        return jsonify({"message": "Image file not provided"}), 400


@app.route('/zoo/<int:entity_id>', methods=['PUT'])
def update_entity(entity_id):
    with app.app_context():
        entity = ZooEntity.query.get(entity_id)
        if entity:
            data = request.get_json()
            entity.color = data['color']
            entity.age = data['age']
            entity.image = data.get('image')
            db.session.commit()
            return jsonify({"message": "Entity updated successfully"})
        else:
            return jsonify({"message": "Entity not found"}), 404

@app.route('/zoo/<int:entity_id>', methods=['DELETE'])
def delete_entity(entity_id):
    with app.app_context():
        entity = ZooEntity.query.get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return jsonify({"message": "Entity deleted successfully"})
        else:
            return jsonify({"message": "Entity not found"}), 404

# User Routes

@app.route('/users', methods=['GET'])
def get_all_users():
    with app.app_context():
        users = User.query.all()
        result = [
            {"id": user.id, "name": user.name, "email": user.email}
            for user in users
        ]
    return jsonify(result)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    with app.app_context():
        user = User.query.get(user_id)
        if user:
            result = {"id": user.id, "name": user.name, "email": user.email}
            return jsonify(result)
        else:
            return jsonify({"message": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    with app.app_context():
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
    return jsonify({"message": "User added successfully"}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    with app.app_context():
        user = User.query.get(user_id)
        if user:
            data = request.get_json()
            user.name = data['name']
            user.email = data['email']
            db.session.commit()
            return jsonify({"message": "User updated successfully"})
        else:
            return jsonify({"message": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    with app.app_context():
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User deleted successfully"})
        else:
            return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
