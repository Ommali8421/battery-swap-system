from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_data):
        self.id = user_data[0]
        self.username = user_data[1]
        self.email = user_data[2]
        self.password_hash = user_data[3]
        self.role = user_data[4]
