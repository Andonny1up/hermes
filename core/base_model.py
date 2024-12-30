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


    def execute(self, query_text,**params):
        """
        Ejecuta una consulta SQL con parámetros nombrados.
        :param query_text: La consulta SQL a ejecutar.
        :param params: Los parámetros nombrados de la consulta.
        :return: Un objeto QSqlQuery con el resultado de la ejecución.
        """
        query = QSqlQuery(self.db)
        query.prepare(query_text)

        # Asociar los parámetros nombrados con la consulta
        for key, value in params.items():
            query.bindValue(f":{key}", value)

        if not query.exec():
            raise RuntimeError(f"Error ejecutando la consulta: {query.lastError().text()}")

        return query

    def create(self, **fields):
        """
        Insertar un registro en la tabla del modelo.
        :param fields: diccionario con los parametros y valores.
        """
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
