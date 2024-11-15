from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class ComponentsPanel(QWidget):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #eaeaea; border-right: 1px solid #ccc;")
        self.setFixedWidth(200)

        # Vertical layout for the panel
        layout = QVBoxLayout(self)

        # Add prebuilt components (button, label)
        add_button = QPushButton("Add Button")
        add_button.clicked.connect(self.add_button_to_canvas)
        layout.addWidget(add_button)

        add_label = QPushButton("Add Label")
        add_label.clicked.connect(self.add_label_to_canvas)
        layout.addWidget(add_label)

    def add_button_to_canvas(self):
        """Adds a Button to the canvas."""
        new_button = QPushButton("Button")
        self.canvas.add_component(new_button)

    def add_label_to_canvas(self):
        """Adds a Label to the canvas."""
        new_label = QLabel("Label")
        self.canvas.add_component(new_label)
