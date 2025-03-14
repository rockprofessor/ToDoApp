import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from todo_app import TodoApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    
    # Ensure window is visible and active
    window.setWindowState(Qt.WindowState.WindowActive)
    window.show()
    window.raise_()
    window.activateWindow()
    
    sys.exit(app.exec())