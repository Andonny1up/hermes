from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QWidget
from interfaces.ui_login import Ui_LoginUI


class login_v(QWidget, Ui_LoginUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Eliminar los bordes de la ventana
        self.setWindowFlags(Qt.FramelessWindowHint)
        # Hacer el fondo translúcido
        self.setAttribute(Qt.WA_TranslucentBackground)

        # botones
        self.closeBtn.clicked.connect(self.close_app)

        # Variables para arrastrar
        self._dragging = False
        self._start_pos = QPoint()

    def mousePressEvent(self, event):
        # Detectar si el clic fue en la barra (label_2)
        if event.button() == Qt.LeftButton and self.label_2.geometry().contains(event.pos()):
            self._dragging = True
            self._start_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._dragging:
            self.move(event.globalPosition().toPoint() - self._start_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._dragging = False
            event.accept()

    def close_app(self):
        """Cerrar la Aplicación"""
        self.close()
