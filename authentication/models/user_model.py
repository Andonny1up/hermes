from PySide6.QtSql import QSqlDatabase, QSqlQuery
from typing import Optional
from core import base_model


class User(base_model.BaseModel):
    table_name = "users"

    def __init__(self, db, parent=None):
        super().__init__(db, parent)
