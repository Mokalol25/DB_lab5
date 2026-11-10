from flask import Blueprint, request
from app.my_project.auth.dao.user_dao import UserDAO
from app.my_project.auth.service.user_service import UserService
from app.my_project.auth.controller.user_controller import UserController
import yaml

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "25@_SvR_%27",
    "database": "discord_game_db_lab3"
}

user_bp = Blueprint('user', __name__, url_prefix='/api/users')
user_controller = UserController(UserService(UserDAO(db_config)))

@user_bp.route('', methods=['GET'])
def get_users():
    return user_controller.get_all()

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return user_controller.get_by_id(user_id)

@user_bp.route('', methods=['POST'])
def create_user():
    return user_controller.create(request.json)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return user_controller.update(user_id, request.json)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return user_controller.delete(user_id)




@user_bp.route('/insert-nonames', methods=['POST'])
def insert_nonames():
    return user_controller.insert_10_nonames()

@user_bp.route('/run-cursor', methods=['POST'])
def run_cursor():
    return user_controller.run_cursor_split()