from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #f9f9f9; border: 1px solid #ccc;")
        self.setMinimumSize(600, 400)

        # Layout for showing added components (can be improved for drag-and-drop later)
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)

    def add_component(self, component_widget):
        """Adds a component to the canvas."""
        self.layout.addWidget(component_widget)
