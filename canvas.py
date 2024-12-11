from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QGraphicsView, QGraphicsScene, 
    QPushButton, QWidget, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QFont

class CanvasView(QGraphicsView):
    """
    Custom QGraphicsView to implement zoom in and zoom out functionality.
    """
    def __init__(self, scene):
        super().__init__(scene)
        self.scale_factor = 1.0  # Keep track of current zoom level

    def zoom_in(self):
        """
        Zoom in by scaling the view.
        """
        self.scale(1.2, 1.2)
        self.scale_factor *= 1.2

    def zoom_out(self):
        """
        Zoom out by scaling the view.
        """
        self.scale(1 / 1.2, 1 / 1.2)
        self.scale_factor /= 1.2


class CanvasMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Canvas with Zoom - Figma Style")
        self.resize(900, 600)

        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouts for canvas and controls
        layout = QVBoxLayout(central_widget)
        canvas_layout = QHBoxLayout()

        # Create the scene (canvas area)
        scene = QGraphicsScene()
        scene.setBackgroundBrush(QBrush(QColor(240, 240, 240)))
        scene.setSceneRect(-500, -500, 1000, 1000)  # Larger canvas area

        # Add a rectangle to simulate an element in the canvas
        scene.addRect(-100, -100, 200, 200, brush=QBrush(QColor(173, 216, 230)))

        # Add text on the canvas
        text_item = scene.addText("This is a canvas!", QFont("Arial", 14))
        text_item.setDefaultTextColor(QColor("black"))

        # Add a view for the scene
        self.view = CanvasView(scene)
        self.view.setDragMode(QGraphicsView.ScrollHandDrag)
        # self.view.setRenderHint(self.view.renderHints() | Qt.Antialiasing)  # Enable antialiasing
        canvas_layout.addWidget(self.view)

        # Control buttons for zoom
        control_layout = QHBoxLayout()
        zoom_in_button = QPushButton("+")
        zoom_in_button.setStyleSheet(self.button_style())
        zoom_in_button.clicked.connect(self.view.zoom_in)
        control_layout.addWidget(zoom_in_button)

        zoom_out_button = QPushButton("-")
        zoom_out_button.setStyleSheet(self.button_style())
        zoom_out_button.clicked.connect(self.view.zoom_out)
        control_layout.addWidget(zoom_out_button)

        # Add canvas and controls to main layout
        layout.addLayout(canvas_layout)
        layout.addLayout(control_layout)

    def button_style(self):
        """
        Apply modern button style.
        """
        return """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                border: none;
                border-radius: 5px;
                padding: 10px;
                width: 40px;
                height: 40px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """


# if __name__ == "__main__":
#     app = QApplication([])
#     window = CanvasMainWindow()
#     window.show()
#     app.exec()
