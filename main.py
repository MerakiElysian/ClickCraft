import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

# Import other modules
from canvas import Canvas
from components import ComponentsPanel

class ClickCraftApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set main window properties
        self.setWindowTitle("ClickCraft - GUI Builder")
        self.setGeometry(100, 100, 800, 600)

        # Create the central widget and layout
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        # Add Canvas and Components Panel
        self.canvas = Canvas(self)
        self.components_panel = ComponentsPanel(self.canvas)

        # Add to layout
        main_layout.addWidget(self.components_panel)
        main_layout.addWidget(self.canvas)

        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ClickCraftApp()
    main_window.show()
    sys.exit(app.exec_())
