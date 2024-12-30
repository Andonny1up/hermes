from PySide6.QtSql import QSqlDatabase
from authentication.models.user_model import User
from helpers import abs_path
from PySide6.QtCore import QCoreApplication
# Configurar la conexión a la base de datos


def create_connection():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(abs_path("database/hermes.db"))
    if not db.open():
        raise Exception("No se pudo abrir la base de datos")
    return db


# Main
if __name__ == "__main__":
    app = QCoreApplication([])
    db = create_connection()

    # Crear un modelo de usuario
    user_model = User(db)

    # Crear un usuario
    # user_id = user_model.create_user(
    #     username="andoni", password="and123456")
    # print(f"Usuario creado con ID: {user_id}")

    username="andoni"
    password="and123456"

    if user_model.authenticate(username, password):
        print("Usuario autenticado correctamente.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

    # # Obtener el usuario creado
    # user = user_model.get(user_id)
    # print("Usuario obtenido:", user)

    # # Actualizar el usuario
    # user_model.update(user_id, email="john_updated@example.com")

    # # Obtener todos los usuarios
    # users = user_model.all()
    # print("Todos los usuarios:", users)

    # # Eliminar el usuario
    # user_model.delete(user_id)
    # print("Usuario eliminado.")
