from app.my_project.auth.dao.user_dao import UserDAO

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, user_id):
        return self.dao.get_by_id(user_id)

    def create(self, data):
        return self.dao.create(
            username=data.get('username'),
            email=data.get('email'),
            password_hash=data.get('password_hash')
        )

    def update(self, user_id, data):
        return self.dao.update(
            user_id=user_id,
            username=data.get('username'),
            email=data.get('email')
        )

    def delete(self, user_id):
        return self.dao.delete(user_id)