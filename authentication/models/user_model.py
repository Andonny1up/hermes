import bcrypt
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from typing import Optional
from core import base_model


class User(base_model.BaseModel):
    table_name = "users"

    def __init__(self, db, parent=None):
        super().__init__(db, parent)


    def create_user(self, username, password):
        """crear usuario con contraseña encriptada"""

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.create(username=username, password=hashed_password.decode('utf-8'))


    def authenticate(self, username: str, password: str):
        """ Autentificar al usuario """
        query = self.execute(f"SELECT * FROM {self.table_name} WHERE username = :username", username=username)
        if query.next():
            stored_hash = query.value(2)
            print(query.value(2))
            if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                return True
        return False
