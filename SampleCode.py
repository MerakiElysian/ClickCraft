#------------------This code is  use to divide the window into three frames----------------

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QFormLayout, QSplitter,
    QListWidget, QGraphicsView, QWidget, QLabel, QPushButton, QLineEdit, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor

class AdvancedClickCraftApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Main Window Setup
        self.setWindowTitle("ClickCraft - Advanced GUI Builder")
        self.setGeometry(100, 100, 1400, 900)
        
        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main Layout
        main_layout = QHBoxLayout(central_widget)

        # Components Section
        components_frame = QFrame()
        components_frame.setFrameShape(QFrame.StyledPanel)
        components_frame.setFrameShadow(QFrame.Raised)
        components_layout = QVBoxLayout(components_frame)

        components_title = QLabel("Components")
        components_title.setFont(QFont("Arial", 14, QFont.Bold))
        components_title.setAlignment(Qt.AlignCenter)
        components_list = QListWidget()
        components_list.addItems(["Button", "Label", "Input Field", "Checkbox", "Dropdown", "Radio Button"])
        components_list.setStyleSheet("background-color: #f0f0f0; font-size: 14px;")
        components_layout.addWidget(components_title)
        components_layout.addWidget(components_list)

        # Canvas Section
        canvas_frame = QFrame()
        canvas_frame.setFrameShape(QFrame.StyledPanel)
        canvas_frame.setFrameShadow(QFrame.Raised)
        canvas_layout = QVBoxLayout(canvas_frame)

        canvas_title = QLabel("Canvas")
        canvas_title.setFont(QFont("Arial", 14, QFont.Bold))
        canvas_title.setAlignment(Qt.AlignCenter)
        canvas_area = QGraphicsView()
        canvas_area.setStyleSheet("background-color: #e8e8e8; border: 2px solid #cccccc;")
        canvas_layout.addWidget(canvas_title)
        canvas_layout.addWidget(canvas_area)

        # Properties Section
        properties_frame = QFrame()
        properties_frame.setFrameShape(QFrame.StyledPanel)
        properties_frame.setFrameShadow(QFrame.Raised)
        properties_layout = QVBoxLayout(properties_frame)

        properties_title = QLabel("Properties")
        properties_title.setFont(QFont("Arial", 14, QFont.Bold))
        properties_title.setAlignment(Qt.AlignCenter)
        properties_form = QFormLayout()
        properties_form.setLabelAlignment(Qt.AlignRight)
        properties_form.setFormAlignment(Qt.AlignCenter)

        prop_selected_label = QLabel("Selected:")
        prop_selected_value = QLabel("None")
        prop_width_label = QLabel("Width:")
        prop_width_input = QLineEdit()
        prop_height_label = QLabel("Height:")
        prop_height_input = QLineEdit()
        update_button = QPushButton("Apply Changes")
        update_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 14px; padding: 5px;")

        properties_form.addRow(prop_selected_label, prop_selected_value)
        properties_form.addRow(prop_width_label, prop_width_input)
        properties_form.addRow(prop_height_label, prop_height_input)
        properties_layout.addWidget(properties_title)
        properties_layout.addLayout(properties_form)
        properties_layout.addWidget(update_button)

        # Splitter for resizing
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(components_frame)
        splitter.addWidget(canvas_frame)
        splitter.addWidget(properties_frame)
        splitter.setStretchFactor(1, 3)  # Give more space to the canvas
        splitter.setStyleSheet("QSplitter::handle { background: #ccc; width: 3px; }")

        # Add splitter to main layout
        main_layout.addWidget(splitter)

        # Add some styles to make UI more advanced
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffffff;
            }
            QLabel {
                color: #333333;
            }
            QPushButton {
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #dcdcdc;
            }
            QLineEdit {
                border: 1px solid #cccccc;
                border-radius: 3px;
                padding: 5px;
            }
        """)


if __name__ == "__main__":
    app = QApplication([])
    window = AdvancedClickCraftApp()
    window.show()
    app.exec_()

#--------------------------