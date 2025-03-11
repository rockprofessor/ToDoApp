#JOhni12 was here too, geht das? 
#Hello
# Emil was here :D
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox
import sys

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do App")
        self.setGeometry(300, 300, 400, 400)

        self.layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task")
        self.layout.addWidget(self.task_input)

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        self.remove_button = QPushButton("Remove Task")
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)
        
        self.pro_abo_button = QPushButton("Pro Abo")
        self.pro_abo_button.clicked.connect(self.pro_abo)
        self.layout.addWidget(self.pro_abo_button)

        self.setLayout(self.layout)

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")

    def remove_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            self.task_list.takeItem(selected)
        else:
            QMessageBox.warning(self, "Warning", "Select a task to remove!")
    
    def pro_abo(self):
        QMessageBox.information(self, "Pro Abo", "Upgrade to Pro for more features!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())

