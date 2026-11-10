import mysql.connector

class UserDAO:
    def __init__(self, config):
        self.config = config

    def _get_connection(self):
        return mysql.connector.connect(**self.config)

    def get_all(self):
        with self._get_connection() as db:
            with db.cursor(dictionary=True) as cursor:  
                cursor.execute("SELECT id, username, email, created_at FROM users")
                return cursor.fetchall()

    def get_by_id(self, user_id):
        with self._get_connection() as db:
            with db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, username, email, created_at FROM users WHERE id = %s", (user_id,))
                return cursor.fetchone()

    def create(self, username, email, password_hash):
        with self._get_connection() as db:
            with db.cursor() as cursor:
                query = "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)"
                cursor.execute(query, (username, email, password_hash))
                db.commit()
                return cursor.lastrowid

    def update(self, user_id, username, email):
        with self._get_connection() as db:
            with db.cursor() as cursor:
                query = "UPDATE users SET username = %s, email = %s WHERE id = %s"
                cursor.execute(query, (username, email, user_id))
                db.commit()
                return cursor.rowcount

    def delete(self, user_id):
        with self._get_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                db.commit()
                return cursor.rowcount
    
    
    
    
    def insert_10_nonames(self):
        with self._get_connection() as db:
            with db.cursor() as cursor:
                # Викликаємо процедуру без параметрів
                cursor.callproc('insert_10_nonames')
                db.commit()
                return True

    def run_cursor_split(self):
        with self._get_connection() as db:
            with db.cursor() as cursor:
                # Викликаємо процедуру з курсором
                cursor.callproc('cursor_random_split')
                db.commit()
                return True