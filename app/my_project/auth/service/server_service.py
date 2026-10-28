from app.my_project.auth.dao.server_dao import ServerDAO

class ServerService:
    def __init__(self, dao: ServerDAO):
        self.dao = dao

    def get_server_channels(self, server_id):
        return self.dao.get_channels_by_server(server_id)
    
    
    def get_server_members(self, server_id):
        return self.dao.get_members_by_server(server_id)