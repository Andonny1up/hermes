from authentication.models.user_model import User

class UserController:
    def __init__(self,db):
        self.db = db
        self.model = User(self.db)