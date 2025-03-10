#JOhni12 was here too, i try to 
#Hello
# Emil was here :D
#Simon wasn't here :(

# test 3
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox, QComboBox, QDateTimeEdit
from PyQt6.QtCore import QDateTime, QTimer
import sys

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do & Reminder App")
        self.setGeometry(300, 300, 500, 500)

        self.layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task")
        self.layout.addWidget(self.task_input)

        self.date_time_input = QDateTimeEdit(self)
        self.date_time_input.setDateTime(QDateTime.currentDateTime())
        self.layout.addWidget(self.date_time_input)

        self.category_select = QComboBox(self)
        self.category_select.addItems(["Schule", "Privat"])
        self.layout.addWidget(self.category_select)

        self.priority_select = QComboBox(self)
        self.priority_select.addItems(["Hoch", "Mittel", "Niedrig"])
        self.layout.addWidget(self.priority_select)

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        self.remove_button = QPushButton("Remove Task")
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)

        self.setLayout(self.layout)
        self.reminders = []
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_reminders)
        self.timer.start(60000)  # Check every minute

    def add_task(self):
        task = self.task_input.text().strip()
        date_time = self.date_time_input.dateTime()
        category = self.category_select.currentText()
        priority = self.priority_select.currentText()

        if task:
            task_entry = f"{task} - {category} - {priority} - {date_time.toString()}"
            self.task_list.addItem(task_entry)
            self.reminders.append((task, date_time, category, priority))
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")

    def remove_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            self.task_list.takeItem(selected)
            del self.reminders[selected]
        else:
            QMessageBox.warning(self, "Warning", "Select a task to remove!")

    def check_reminders(self):
        current_time = QDateTime.currentDateTime()
        for task, date_time, category, priority in self.reminders:
            if date_time <= current_time:
                QMessageBox.information(self, "Reminder", f"Erinnerung: {task} ({category})")
                self.reminders.remove((task, date_time, category, priority))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())

