from flask import request, make_response, jsonify, Blueprint
from app import db
from app.models.user import User

user_bp = Blueprint('user_bp', __name__)

# create a user
@user_bp.post('/users')
def create_user():
  try:
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({'message': 'user created'}), 201)
  except Exception as e:
    print(e)
    return make_response(jsonify({'message': 'error creating user'}), 500)

# get all users
@user_bp.get('/users')
def get_users():
  try:
    users = User.query.all()
    return make_response(jsonify([user.json() for user in users]), 200)
  except Exception as e:
    print(e)
    return make_response(jsonify({'message': 'error getting users'}), 500)

@user_bp.get('/users/<int:id>')
def get_user(id):
  try:
    user = db.get_or_404(User, id)
    return make_response(jsonify(user.json()), 200)
  except Exception as e:
    return make_response(jsonify({'message': 'User Not Found'}), 404)