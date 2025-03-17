from textual.app import App, ComposeResult 
from textual.widgets import Header, Footer, Input, Static, Button, ListView, ListItem 
from textual.containers import Vertical
from datetime import datetime
import argparse

#Argument parser for parsing arguments
parser = argparse.ArgumentParser(
	description = "Import existing taskfile or -p to only print all tasks"
)

# Group for adding tasks: -ti (adds a tasks), -tf (add tasks from a file)
task_group = parser.add_mutually_exclusive_group(required=False)
task_group.add_argument(
    "-ti", "--task-input",
    help="adds task directly with this argument, Format: 'title, due_date'"
)

task_group.add_argument(
    "-tf", "--task-file",
    help="adds tasks from a file, each line should contain 'title, due_date'"
)

task_group.add_argument(
    "-p", "--print",
    help="prints all tasks",
    action = "store_true"
)




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
    args = parser.parse_args()
    
    if args.task_input:
        parts = [part.strip() for part in args.task_input.split(',', 1)]
        try:
            task = Task(parts[0], parts[1])
            print(task)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    elif args.task_file:
        with open(args.task_file, 'r') as file:
            for line in file:
                parts = [part.strip() for part in line.strip().split(',', 1)]
                try:
                    task = Task(parts[0], parts[1])
                    print(task)
                except ValueError:
                    print(f"Invalid date format for task '{parts[0]}'. Please use YYYY-MM-DD.")

    elif args.print:
        # Assuming tasks are stored in a file named 'tasks.txt'
        with open('tasks.txt', 'r') as file:
            for line in file:
                parts = [part.strip() for part in line.strip().split(',', 1)]
                try:
                    task = Task(parts[0], parts[1])
                    print(task)
                except ValueError:
                    print(f"Invalid date format for task '{parts[0]}'. Please use YYYY-MM-DD.")
                except FileNotFoundError:
                    print("No tasks found. Please add tasks using -ti or -tf or using the interface.")
    else:
        app = TodoApp()
        app.run()
