from PyQt5.QtWidgets import (
    QApplication, QTabWidget, QWidget, QVBoxLayout, QLabel,
    QMainWindow, QMenuBar, QMenu, QAction, QFileDialog, QMessageBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Widget with Menu Bar")
        self.resize(600, 400)

        # Create the menu bar
        self.create_menu_bar()

    def create_menu_bar(self):
        """
        Create the menu bar with Save, Open, and Export functions.
        """
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # File menu
        file_menu = QMenu("File", self)
        menu_bar.addMenu(file_menu)

        # Actions for the File menu
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        export_action = QAction("Export", self)
        export_action.triggered.connect(self.export_file)
        file_menu.addAction(export_action)

        # Help menu
        help_menu = QMenu("Help", self)
        menu_bar.addMenu(help_menu)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def open_file(self):
        """
        Open a file using QFileDialog.
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        if file_path:
            QMessageBox.information(self, "File Opened", f"Opened: {file_path}")

    def save_file(self):
        """
        Save a file using QFileDialog.
        """
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            QMessageBox.information(self, "File Saved", f"Saved: {file_path}")

    def export_file(self):
        """
        Export functionality (placeholder).
        """
        QMessageBox.information(self, "Export", "Export functionality triggered!")

    def show_about(self):
        """
        Show About dialog.
        """
        QMessageBox.about(self, "About", "This is a Tab Widget application with a menu bar.\nCreated using PyQt5.")

# Run the application
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
