from flask import jsonify

class UserController:
    def __init__(self, service):
        self.service = service

    def get_all(self):
        return jsonify(self.service.get_all()), 200

    def get_by_id(self, user_id):
        user = self.service.get_by_id(user_id)
        if user:
            return jsonify(user), 200
        return jsonify({"message": "Користувача не знайдено"}), 404

    def create(self, data):
        if not all(k in data for k in ("username", "email", "password_hash")):
            return jsonify({"message": "Відсутні обов'язкові поля"}), 400
        
        user_id = self.service.create(data)
        return jsonify({"id": user_id, "message": "Користувача створено"}), 201

    def update(self, user_id, data):
        if not all(k in data for k in ("username", "email")):
            return jsonify({"message": "Відсутні поля для оновлення"}), 400

        updated_rows = self.service.update(user_id, data)
        if updated_rows > 0:
            return jsonify({"message": "Дані користувача оновлено"}), 200
        return jsonify({"message": "Користувача не знайдено або дані ідентичні"}), 404

    def delete(self, user_id):
        deleted_rows = self.service.delete(user_id)
        if deleted_rows > 0:
            return jsonify({"message": "Користувача видалено"}), 200
        return jsonify({"message": "Користувача не знайдено"}), 404