from flask import Blueprint
from app.my_project.auth.dao.server_dao import ServerDAO
from app.my_project.auth.service.server_service import ServerService
from app.my_project.auth.controller.server_controller import ServerController
import yaml

with open('app/config/app.yml', 'r', encoding='utf-8') as f:
    db_config = yaml.safe_load(f)['db']

server_bp = Blueprint('server', __name__, url_prefix='/api/servers')
server_controller = ServerController(ServerService(ServerDAO(db_config)))

@server_bp.route('/<int:server_id>/channels', methods=['GET'])
def get_server_channels(server_id):
    return server_controller.get_channels(server_id)


@server_bp.route('/<int:server_id>/members', methods=['GET'])
def get_server_members(server_id):
    return server_controller.get_members(server_id)