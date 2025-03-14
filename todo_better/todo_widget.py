from PyQt6.QtWidgets import (
    QFrame, QHBoxLayout, QCheckBox, 
    QLabel, QPushButton, QLineEdit
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont

class TodoWidget(QFrame):
    toggled = pyqtSignal(int)  # Signal für das Umschalten des Todo-Status
    edited = pyqtSignal(int, str)  # Signal für das Bearbeiten des Todo-Texts
    deleted = pyqtSignal(int)  # Signal für das Löschen des Todos
    
    def __init__(self, todo, parent=None):
        super().__init__(parent)
        self.todo = todo
        self.setObjectName("todo-item")
        self.setProperty("completed", todo.completed)
        
        # Layout
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 10, 10, 10)
        
        # Checkbox
        self.checkbox = QCheckBox()
        self.checkbox.setChecked(todo.completed)
        self.checkbox.stateChanged.connect(self._on_toggle)
        
        # Text Label (normal mode)
        self.text_label = QLabel(todo.text)
        self.text_label.setObjectName("todo-text")
        if todo.completed:
            font = self.text_label.font()
            font.setStrikeOut(True)
            self.text_label.setFont(font)
        
        # Edit Input (edit mode)
        self.edit_input = QLineEdit(todo.text)
        self.edit_input.setObjectName("todo-edit")
        self.edit_input.returnPressed.connect(self._save_edit)
        self.edit_input.hide()
        
        # Buttons Container
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(5)
        
        # Edit Button
        self.edit_button = QPushButton("Bearbeiten")
        self.edit_button.setObjectName("edit-button")
        self.edit_button.clicked.connect(self._start_edit)
        self.edit_button.setEnabled(not todo.completed)
        
        # Save Button (edit mode)
        self.save_button = QPushButton("Speichern")
        self.save_button.setObjectName("save-button")
        self.save_button.clicked.connect(self._save_edit)
        self.save_button.hide()
        
        # Cancel Button (edit mode)
        self.cancel_button = QPushButton("Abbrechen")
        self.cancel_button.setObjectName("cancel-button")
        self.cancel_button.clicked.connect(self._cancel_edit)
        self.cancel_button.hide()
        
        # Delete Button
        self.delete_button = QPushButton("Löschen")
        self.delete_button.setObjectName("delete-button")
        self.delete_button.clicked.connect(lambda: self.deleted.emit(self.todo.id))
        
        # Buttons zum Layout hinzufügen
        buttons_layout.addWidget(self.edit_button)
        buttons_layout.addWidget(self.save_button)
        buttons_layout.addWidget(self.cancel_button)
        buttons_layout.addWidget(self.delete_button)
        
        # Alles zum Hauptlayout hinzufügen
        self.layout.addWidget(self.checkbox)
        self.layout.addWidget(self.text_label, 1)  # 1 = stretch factor
        self.layout.addWidget(self.edit_input, 1)
        self.layout.addLayout(buttons_layout)
    
    def _on_toggle(self):
        # Sende Signal zum Umschalten des Todo-Status
        self.toggled.emit(self.todo.id)
        
        # Aktualisiere die Darstellung
        completed = self.checkbox.isChecked()
        self.setProperty("completed", completed)
        self.style().unpolish(self)
        self.style().polish(self)
        
        # Durchstreichen des Textes
        font = self.text_label.font()
        font.setStrikeOut(completed)
        self.text_label.setFont(font)
        
        # Deaktiviere Bearbeiten-Button, wenn erledigt
        self.edit_button.setEnabled(not completed)
    
    def _start_edit(self):
        # Wechsle in den Bearbeitungsmodus
        self.text_label.hide()
        self.edit_input.show()
        self.edit_input.setFocus()
        self.edit_button.hide()
        self.delete_button.hide()
        self.save_button.show()
        self.cancel_button.show()
    
    def _save_edit(self):
        # Speichere die Änderungen
        new_text = self.edit_input.text().strip()
        if new_text:
            self.edited.emit(self.todo.id, new_text)
            self.text_label.setText(new_text)
        
        # Zurück zum normalen Modus
        self._exit_edit_mode()
    
    def _cancel_edit(self):
        # Verwerfe die Änderungen
        self.edit_input.setText(self.todo.text)
        
        # Zurück zum normalen Modus
        self._exit_edit_mode()
    
    def _exit_edit_mode(self):
        self.text_label.show()
        self.edit_input.hide()
        self.edit_button.show()
        self.delete_button.show()
        self.save_button.hide()
        self.cancel_button.hide()