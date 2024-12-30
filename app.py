""" app main """
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from authentication.views.login_v import login_v

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('static/logo-Hermes-icon.png'))
    window = login_v()
    window.show()
    sys.exit(app.exec_())
