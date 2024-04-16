from flask_login import UserMixin
from flask import url_for


class UserLoader(UserMixin):
    def from_db(self, user_id, db):
        self.__user = db.get_user(user_id)
        return self
