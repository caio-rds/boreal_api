from fastapi import HTTPException
from database.database import Database
from service.auth import AuthHandler

auth_handler = AuthHandler()


class LoginController:
    def __init__(self):
        self.db = Database()

    # return if passed username actually exists in database
    def user_exists(self, username: str):
        result = self.db.get_user_data(username)
        if result:
            if result[1] == username:
                return True

        return False

    # after user_exists() return TRUE, login-view will pass username and password here
    # and will be validated if everything is ok
    def autorize_login(self, username: str, password: str):
        user_id, user_name, hashed_password = self.db.get_user_data(username)

        if not auth_handler.verify_password(password, hashed_password):
            raise HTTPException(status_code=401, detail='Invalid username and/or password')
        token = auth_handler.encode_token(username)
        return {'acess_token': token}
