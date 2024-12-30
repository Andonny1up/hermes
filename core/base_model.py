from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtCore import QObject


class BaseModel(QObject):
    """ clase base, Para reutilizar la funcion Create, Update, Get entre otras"""
    table_name = None

    def __init__(self, db: QSqlDatabase, parent=None):
        super().__init__(parent)
        if not db.isOpen():
            raise ConnectionError(
                'No se ha podido conectar con la base de datos')
        self.db = db

    def create(self, **fields):
        """Insertar un registro en la tabla del modelo"""
        keys = ", ".join(fields.keys())
        placeholders = ", ".join([f":{key}" for key in fields.keys()])
        query = QSqlQuery(self.db)
        query.prepare(
            f"INSERT INTO {self.table_name} ({keys}) VALUES ({placeholders})")

        for key, value in fields.items():
            query.addBindValue(value)

        if not query.exec():
            raise ValueError(
                f"Error al crear el registro: {query.lastError().text()}")

        return query.lastInsertId()
