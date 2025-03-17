from textual.app import App, ComposeResult from textual.widgets import Header, Footer, Input, Static, Button, ListView, ListItem from textual.containers import Vertical
from datetime import datetime

class Task:
    def __init__(self, title: str, due_date: str):
        self.title = title
        try:
            self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            self.due_date = None

    def __str__(self):
        due = self.due_date.strftime("%Y-%m-%d") if self.due_date else "No Date"
        return f"{self.title} (Due: {due})"

class TaskItem(ListItem):
    def __init__(self, task: Task):
        super().__init__(Static(str(task)))
        self.data = task  # store the task object safely

class TodoApp(App):
    CSS_PATH = None
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Enter task title and due date (YYYY-MM-DD):")
        yield Input(placeholder="Task Title", id="title_input")
        yield Input(placeholder="Due Date (YYYY-MM-DD)", id="date_input")
        yield Button("Add Task", id="add_btn")
        yield Static("Tasks:")
        yield ListView(id="task_list")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add_btn":
            title = self.query_one("#title_input", Input).value.strip()
            date_str = self.query_one("#date_input", Input).value.strip()

            if title:
                task = Task(title, date_str)
                task_list = self.query_one("#task_list", ListView)
                task_list.append(TaskItem(task))
                self.query_one("#title_input", Input).value = ""
                self.query_one("#date_input", Input).value = ""

if __name__ == "__main__":
    app = TodoApp()
    app.run()

