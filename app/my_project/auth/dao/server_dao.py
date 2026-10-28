import mysql.connector

class ServerDAO:
    def __init__(self, config):
        self.config = config

    def _get_connection(self):
        return mysql.connector.connect(**self.config)

    def get_channels_by_server(self, server_id):
        with self._get_connection() as db:
            with db.cursor(dictionary=True) as cursor:
                query = """
                    SELECT c.id, c.name AS channel_name, c.channel_type, s.name AS server_name 
                    FROM channels c
                    JOIN servers s ON c.server_id = s.id
                    WHERE s.id = %s
                """
                cursor.execute(query, (server_id,))
                return cursor.fetchall()
          
            
    def get_members_by_server(self, server_id):
        with self._get_connection() as db:
            with db.cursor(dictionary=True) as cursor:
                query = """
                    SELECT u.id AS user_id, u.username, u.email, sm.joined_at
                    FROM users u
                    JOIN server_members sm ON u.id = sm.user_id
                    WHERE sm.server_id = %s
                """
                cursor.execute(query, (server_id,))
                return cursor.fetchall()