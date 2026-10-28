from flask import jsonify

class ServerController:
    def __init__(self, service):
        self.service = service

    def get_channels(self, server_id):
        channels = self.service.get_server_channels(server_id)
        if channels:
            return jsonify(channels), 200
        return jsonify({"message": "Канали не знайдено або сервер не існує"}), 404
    
    
    
    def get_members(self, server_id):
        members = self.service.get_server_members(server_id)
        if members:
            return jsonify(members), 200
        return jsonify({"message": "Учасників не знайдено або сервер не існує"}), 404