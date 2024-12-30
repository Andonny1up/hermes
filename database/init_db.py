""" Create DataBase """
from helpers import abs_path
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtCore import QCoreApplication


def inicialize_database():
    """ Inicialize hermes database"""
    # Crea una instancia de QCoreApplication
    app = QCoreApplication([])

    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(abs_path("database/hermes.db"))

    if not connection.open():
        raise ConnectionError("No se pudo conectar a la base de datos.")

    # create user table
    query = QSqlQuery()
    query.exec("DROP TABLE IF EXISTS users")
    query.exec("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            username VARCHAR(40) UNIQUE NOT NULL,
            password VARCHAR(50) NOT NULL,
            is_active BOOLEAN DEFAULT 1
        )
    """)
    print('siii')
    connection.close()


if __name__ == '__main__':
    inicialize_database()
