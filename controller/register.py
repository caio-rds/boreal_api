from database.database import Database
from service.auth import AuthHandler

auth_handler = AuthHandler()


class RegisterController:
    def __init__(self):
        self.db = Database()

    def insert_user(self, username, password):
        user_db = self.db.get_user_data(data=username)
        # print(username, password)
        if user_db:
            return None
        hashed_password = auth_handler.get_password_hash(password)
        result = self.db.insert_data('user', ('username', 'password'), (username, hashed_password))
        print(result)
        if result:
            return result


