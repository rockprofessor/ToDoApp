import json
import os
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QLineEdit, QFrame, QStackedWidget,
    QScrollArea, QSizePolicy, QGraphicsOpacityEffect
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer, pyqtSlot, QPoint
from PyQt6.QtGui import QFont

from todo_model import Todo  # Korrigierter Import: Todo aus todo_model, nicht todo_widget
from todo_widget import TodoWidget
from styles import STYLES

class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Anwendungseigenschaften
        self.setWindowTitle("Todo App")
        self.setMinimumSize(800, 600)
        self.setWindowFlags(Qt.WindowType.Window)  # Ensure it's a proper window
        self.setWindowOpacity(1.0)  # Ensure window starts fully visible
        self.todos = []
        self.current_filter = "all"
        
        # Hauptlayout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)
        
        # Styling anwenden
        self.setStyleSheet(STYLES)
        
        # UI initialisieren
        self._init_ui()
        
        # Todos laden
        self._load_todos()
        
        # No initial animation
        # self._animate_window_open()
    
    def _init_ui(self):
        # Navigation
        self._create_navbar()
        
        # Stacked Widget für verschiedene Seiten
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)
        
        # Seiten erstellen
        #self.home_page = self._create_home_page()
        self.todos_page = self._create_todos_page()
        self.about_page = self._create_about_page()
        self.contact_page = self._create_contact_page()
        
        # Make sure all pages are visible
        #self.home_page.setVisible(True)
        self.todos_page.setVisible(True)
        self.about_page.setVisible(True)
        self.contact_page.setVisible(True)
        
        # Seiten zum Stacked Widget hinzufügen
        #self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.todos_page)
        self.stacked_widget.addWidget(self.about_page)
        self.stacked_widget.addWidget(self.contact_page)
        
        # Set initial page
        self.stacked_widget.setCurrentIndex(0)
        
        # Footer
        self._create_footer()
        
        # Make sure the stacked widget is visible
        self.stacked_widget.setVisible(True)
    
    def _create_navbar(self):
        navbar = QFrame()
        navbar.setObjectName("navbar")
        navbar_layout = QHBoxLayout(navbar)
        
        # Logo
        logo = QLabel("TodoApp")
        logo.setObjectName("logo")
        navbar_layout.addWidget(logo)
        
        # Navigation Buttons
        nav_buttons_layout = QHBoxLayout()
        nav_buttons_layout.setSpacing(10)
        
        home_btn = QPushButton("Home")
        home_btn.setObjectName("nav-button")
        home_btn.clicked.connect(lambda: self._switch_page(0))
        
        todos_btn = QPushButton("Todos")
        todos_btn.setObjectName("nav-button")
        todos_btn.clicked.connect(lambda: self._switch_page(1))
        
        about_btn = QPushButton("Über uns")
        about_btn.setObjectName("nav-button")
        about_btn.clicked.connect(lambda: self._switch_page(2))
        
        contact_btn = QPushButton("Kontakt")
        contact_btn.setObjectName("nav-button")
        contact_btn.clicked.connect(lambda: self._switch_page(3))
        
        # Buttons zum Layout hinzufügen
        #nav_buttons_layout.addWidget(home_btn)
        nav_buttons_layout.addWidget(todos_btn)
        nav_buttons_layout.addWidget(about_btn)
        nav_buttons_layout.addWidget(contact_btn)
        nav_buttons_layout.addStretch()
        
        navbar_layout.addLayout(nav_buttons_layout)
        self.main_layout.addWidget(navbar)
    """   
    def _create_home_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(30)
        
        # Hero Section
        hero_frame = QFrame()
        hero_frame.setObjectName("hero-frame")
        hero_layout = QVBoxLayout(hero_frame)
        hero_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        title = QLabel("Organisiere dein Leben mit unserer Todo-App")
        title.setObjectName("hero-title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        subtitle = QLabel("Einfach, übersichtlich und effektiv. Behalte den Überblick über deine Aufgaben und erreiche deine Ziele.")
        subtitle.setObjectName("hero-subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setWordWrap(True)
        
        start_button = QPushButton("Jetzt starten")
        start_button.setObjectName("cta-button")
        start_button.clicked.connect(lambda: self._switch_page(1))
        
        hero_layout.addWidget(title)
        hero_layout.addWidget(subtitle)
        hero_layout.addWidget(start_button, 0, Qt.AlignmentFlag.AlignCenter)
        
        # Features Section
        features_layout = QHBoxLayout()
        features_layout.setSpacing(20)
        
        # Feature 1
        feature1 = QFrame()
        feature1.setObjectName("feature-card")
        feature1_layout = QVBoxLayout(feature1)
        feature1_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        feature1_title = QLabel("Einfach zu bedienen")
        feature1_title.setObjectName("feature-title")
        feature1_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        feature1_desc = QLabel("Intuitive Benutzeroberfläche für eine reibungslose Erfahrung.")
        feature1_desc.setObjectName("feature-desc")
        feature1_desc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        feature1_desc.setWordWrap(True)
        
        feature1_layout.addWidget(feature1_title)
        feature1_layout.addWidget(feature1_desc)
        
        # Feature 2
        feature2 = QFrame()
        feature2.setObjectName("feature-card")
        feature2_layout = QVBoxLayout(feature2)
        feature2_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        feature2_title = QLabel("Zeitsparend")
        feature2_title.setObjectName("feature-title")
        feature2_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        feature2_desc = QLabel("Organisiere deine Aufgaben effizient und spare wertvolle Zeit.")
        feature2_desc.setObjectName("feature-desc")
        feature2_desc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        feature2_desc.setWordWrap(True)
        
        feature2_layout.addWidget(feature2_title)
        feature2_layout.addWidget(feature2_desc)
        
        # Feature 3
        feature3 = QFrame()
        feature3.setObjectName("feature-card")
        feature3_layout = QVBoxLayout(feature3)
        feature3_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        feature3_title = QLabel("Anpassbar")
        feature3_title.setObjectName("feature-title")
        feature3_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        feature3_desc = QLabel("Passe die App an deine Bedürfnisse an mit verschiedenen Filterfunktionen.")
        feature3_desc.setObjectName("feature-desc")
        feature3_desc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        feature3_desc.setWordWrap(True)
        
        feature3_layout.addWidget(feature3_title)
        feature3_layout.addWidget(feature3_desc)
        
        # Features zum Layout hinzufügen
        features_layout.addWidget(feature1)
        features_layout.addWidget(feature2)
        features_layout.addWidget(feature3)
        
        # Alles zum Hauptlayout hinzufügen
        layout.addWidget(hero_frame)
        layout.addLayout(features_layout)
        
        # Animationen für die Elemente
        QTimer.singleShot(100, lambda: self._animate_fade_in(title))
        QTimer.singleShot(300, lambda: self._animate_fade_in(subtitle))
        QTimer.singleShot(500, lambda: self._animate_fade_in(start_button))
        QTimer.singleShot(700, lambda: self._animate_fade_in(feature1))
        QTimer.singleShot(900, lambda: self._animate_fade_in(feature2))
        QTimer.singleShot(1100, lambda: self._animate_fade_in(feature3))
        
        return page
    """    
    def _create_todos_page(self):
        # Create a scroll area for the entire page
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName("page-scroll")
        
        # Create the main page widget that will be scrollable
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(20)
        
        # Header
        header = QFrame()
        header_layout = QVBoxLayout(header)
        header_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        title = QLabel("Meine Todos")
        title.setObjectName("page-title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        subtitle = QLabel("Verwalte deine Aufgaben und behalte den Überblick.")
        subtitle.setObjectName("page-subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        
        # Todo Input
        input_frame = QFrame()
        input_layout = QHBoxLayout(input_frame)
        
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Neue Aufgabe hinzufügen...")
        self.todo_input.setObjectName("todo-input")
        self.todo_input.returnPressed.connect(self._add_todo)
        
        add_button = QPushButton("Hinzufügen")
        add_button.setObjectName("add-button")
        add_button.clicked.connect(self._add_todo)
        
        input_layout.addWidget(self.todo_input)
        input_layout.addWidget(add_button)
        
        # Filter Buttons
        filter_frame = QFrame()
        filter_layout = QHBoxLayout(filter_frame)
        filter_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        all_button = QPushButton("Alle")
        all_button.setObjectName("filter-button")
        all_button.setProperty("active", True)
        all_button.clicked.connect(lambda: self._filter_todos("all"))
        
        active_button = QPushButton("Aktiv")
        active_button.setObjectName("filter-button")
        active_button.setProperty("active", False)
        active_button.clicked.connect(lambda: self._filter_todos("active"))
        
        completed_button = QPushButton("Erledigt")
        completed_button.setObjectName("filter-button")
        completed_button.setProperty("active", False)
        completed_button.clicked.connect(lambda: self._filter_todos("completed"))
        
        filter_layout.addWidget(all_button)
        filter_layout.addWidget(active_button)
        filter_layout.addWidget(completed_button)
        
        self.filter_buttons = {
            "all": all_button,
            "active": active_button,
            "completed": completed_button
        }
        
        # Todo List Container
        todo_container = QFrame()
        todo_container.setObjectName("todo-container")
        self.todo_list_layout = QVBoxLayout(todo_container)
        self.todo_list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.todo_list_layout.setSpacing(10)
        
        # Add everything to the main layout
        layout.addWidget(header)
        layout.addWidget(input_frame)
        layout.addWidget(filter_frame)
        layout.addWidget(todo_container)
        layout.addStretch()
        
        # Set the page as the scroll area's widget
        scroll_area.setWidget(page)
        
        # Animations for the elements
        QTimer.singleShot(100, lambda: self._animate_fade_in(title))
        QTimer.singleShot(300, lambda: self._animate_fade_in(subtitle))
        QTimer.singleShot(500, lambda: self._animate_fade_in(input_frame))
        QTimer.singleShot(700, lambda: self._animate_fade_in(filter_frame))
        
        return scroll_area
    
    def _create_about_page(self):
        # Create a scroll area for the entire page
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName("page-scroll")
        
        # Create the main page widget that will be scrollable
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(20)
        
        # Header
        header = QFrame()
        header_layout = QVBoxLayout(header)
        
        title = QLabel("Über uns")
        title.setObjectName("page-title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        subtitle = QLabel("Erfahre mehr über unsere Mission und unser Team.")
        subtitle.setObjectName("page-subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        
        # Mission Section
        mission_frame = QFrame()
        mission_frame.setObjectName("content-section")
        mission_layout = QVBoxLayout(mission_frame)
        
        mission_title = QLabel("Unsere Mission")
        mission_title.setObjectName("section-title")
        
        mission_text1 = QLabel("Wir haben TodoApp entwickelt, um Menschen dabei zu helfen, ihren Alltag besser zu organisieren. Unsere Anwendung ist darauf ausgerichtet, eine einfache und intuitive Möglichkeit zu bieten, Aufgaben zu verwalten und den Überblick zu behalten.")
        mission_text1.setObjectName("section-text")
        mission_text1.setWordWrap(True)
        
        mission_text2 = QLabel("Wir glauben, dass Produktivität nicht kompliziert sein muss. Mit den richtigen Werkzeugen kann jeder seine Ziele erreichen und mehr Zeit für die wichtigen Dinge im Leben haben.")
        mission_text2.setObjectName("section-text")
        mission_text2.setWordWrap(True)
        
        mission_layout.addWidget(mission_title)
        mission_layout.addWidget(mission_text1)
        mission_layout.addWidget(mission_text2)
        
        # Team Section
        team_frame = QFrame()
        team_frame.setObjectName("content-section")
        team_layout = QVBoxLayout(team_frame)
        
        team_title = QLabel("Unser Team")
        team_title.setObjectName("section-title")
        
        team_members_layout = QHBoxLayout()
        
        # Team Member 1
        member1_frame = QFrame()
        member1_frame.setObjectName("team-member")
        member1_layout = QVBoxLayout(member1_frame)
        member1_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        member1_name = QLabel("Max Mustermann")
        member1_name.setObjectName("member-name")
        member1_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        member1_role = QLabel("Gründer & CEO")
        member1_role.setObjectName("member-role")
        member1_role.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        member1_desc = QLabel("Max hat TodoApp mit der Vision gegründet, Produktivitätstools für jeden zugänglich zu machen.")
        member1_desc.setObjectName("member-desc")
        member1_desc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        member1_desc.setWordWrap(True)
        
        member1_layout.addWidget(member1_name)
        member1_layout.addWidget(member1_role)
        member1_layout.addWidget(member1_desc)
        
        # Team Member 2
        member2_frame = QFrame()
        member2_frame.setObjectName("team-member")
        member2_layout = QVBoxLayout(member2_frame)
        member2_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        member2_name = QLabel("Anna Schmidt")
        member2_name.setObjectName("member-name")
        member2_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        member2_role = QLabel("Lead-Entwicklerin")
        member2_role.setObjectName("member-role")
        member2_role.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        member2_desc = QLabel("Anna leitet die Entwicklung von TodoApp und sorgt dafür, dass die Anwendung stets reibungslos funktioniert.")
        member2_desc.setObjectName("member-desc")
        member2_desc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        member2_desc.setWordWrap(True)
        
        member2_layout.addWidget(member2_name)
        member2_layout.addWidget(member2_role)
        member2_layout.addWidget(member2_desc)
        
        # Add team members to layout
        team_members_layout.addWidget(member1_frame)
        team_members_layout.addWidget(member2_frame)
        
        team_layout.addWidget(team_title)
        team_layout.addLayout(team_members_layout)
        
        # Add everything to main layout
        layout.addWidget(header)
        layout.addWidget(mission_frame)
        layout.addWidget(team_frame)
        layout.addStretch()
        
        # Set the page as the scroll area's widget
        scroll_area.setWidget(page)
        
        # Animations
        QTimer.singleShot(100, lambda: self._animate_fade_in(title))
        QTimer.singleShot(300, lambda: self._animate_fade_in(subtitle))
        QTimer.singleShot(500, lambda: self._animate_fade_in(mission_frame))
        QTimer.singleShot(700, lambda: self._animate_fade_in(team_frame))
        
        return scroll_area
    
    def _create_contact_page(self):
        # Create a scroll area for the entire page
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName("page-scroll")
        
        # Create the main page widget that will be scrollable
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(20)
        
        # Header
        header = QFrame()
        header_layout = QVBoxLayout(header)
        
        title = QLabel("Kontakt")
        title.setObjectName("page-title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        subtitle = QLabel("Hast du Fragen oder Feedback? Kontaktiere uns!")
        subtitle.setObjectName("page-subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        
        # Contact Content
        contact_layout = QHBoxLayout()
        
        # Contact Info
        info_frame = QFrame()
        info_frame.setObjectName("contact-info")
        info_layout = QVBoxLayout(info_frame)
        
        email_label = QLabel("E-Mail")
        email_label.setObjectName("contact-label")
        email_value = QLabel("info@todoapp.de")
        email_value.setObjectName("contact-value")
        
        phone_label = QLabel("Telefon")
        phone_label.setObjectName("contact-label")
        phone_value = QLabel("+49 123 456789")
        phone_value.setObjectName("contact-value")
        
        address_label = QLabel("Adresse")
        address_label.setObjectName("contact-label")
        address_value = QLabel("Musterstraße 123, 12345 Berlin")
        address_value.setObjectName("contact-value")
        
        info_layout.addWidget(email_label)
        info_layout.addWidget(email_value)
        info_layout.addSpacing(10)
        info_layout.addWidget(phone_label)
        info_layout.addWidget(phone_value)
        info_layout.addSpacing(10)
        info_layout.addWidget(address_label)
        info_layout.addWidget(address_value)
        info_layout.addStretch()
        
        # Contact Form
        form_frame = QFrame()
        form_frame.setObjectName("contact-form")
        form_layout = QVBoxLayout(form_frame)
        
        name_label = QLabel("Name")
        name_label.setObjectName("form-label")
        name_input = QLineEdit()
        name_input.setObjectName("form-input")
        
        email_label = QLabel("E-Mail")
        email_label.setObjectName("form-label")
        email_input = QLineEdit()
        email_input.setObjectName("form-input")
        
        message_label = QLabel("Nachricht")
        message_label.setObjectName("form-label")
        message_input = QLineEdit()
        message_input.setObjectName("form-input")
        
        submit_button = QPushButton("Nachricht senden")
        submit_button.setObjectName("submit-button")
        
        form_layout.addWidget(name_label)
        form_layout.addWidget(name_input)
        form_layout.addSpacing(10)
        form_layout.addWidget(email_label)
        form_layout.addWidget(email_input)
        form_layout.addSpacing(10)
        form_layout.addWidget(message_label)
        form_layout.addWidget(message_input)
        form_layout.addSpacing(20)
        form_layout.addWidget(submit_button)
        
        # Add frames to contact layout
        contact_layout.addWidget(info_frame)
        contact_layout.addWidget(form_frame)
        
        # Add everything to main layout
        layout.addWidget(header)
        layout.addLayout(contact_layout)
        layout.addStretch()
        
        # Set the page as the scroll area's widget
        scroll_area.setWidget(page)
        
        # Animations
        QTimer.singleShot(100, lambda: self._animate_fade_in(title))
        QTimer.singleShot(300, lambda: self._animate_fade_in(subtitle))
        QTimer.singleShot(500, lambda: self._animate_fade_in(info_frame))
        QTimer.singleShot(700, lambda: self._animate_fade_in(form_frame))
        
        return scroll_area
    
    def _create_footer(self):
        footer = QFrame()
        footer.setObjectName("footer")
        footer_layout = QHBoxLayout(footer)
        
        copyright = QLabel(f"© {2023} TodoApp. Alle Rechte vorbehalten.")
        copyright.setObjectName("copyright")
        
        social_layout = QHBoxLayout()
        social_layout.setSpacing(15)
        
        facebook = QPushButton("Facebook")
        facebook.setObjectName("social-button")
        
        twitter = QPushButton("Twitter")
        twitter.setObjectName("social-button")
        
        instagram = QPushButton("Instagram")
        instagram.setObjectName("social-button")
        
        social_layout.addWidget(facebook)
        social_layout.addWidget(twitter)
        social_layout.addWidget(instagram)
        
        footer_layout.addWidget(copyright)
        footer_layout.addStretch()
        footer_layout.addLayout(social_layout)
        
        self.main_layout.addWidget(footer)
    
    def _switch_page(self, index):
        # Animation für den Seitenwechsel
        self.stacked_widget.setCurrentIndex(index)
        
        # Aktualisiere die Filter-Buttons, wenn zur Todo-Seite gewechselt wird
        if index == 1:
            self._update_filter_buttons()
    
    def _add_todo(self):
        text = self.todo_input.text().strip()
        if text:
            todo = Todo(text=text)
            self.todos.append(todo)
            self._save_todos()
            self._refresh_todo_list()
            self.todo_input.clear()
            
            # Animation für das neue Todo
            if self.todo_list_layout.count() > 0:
                last_widget = self.todo_list_layout.itemAt(self.todo_list_layout.count() - 1).widget()
                self._animate_fade_in(last_widget)
    
    def _toggle_todo(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                todo.completed = not todo.completed
                self._save_todos()
                self._refresh_todo_list()
                break
    
    def _edit_todo(self, todo_id, new_text):
        for todo in self.todos:
            if todo.id == todo_id:
                todo.text = new_text
                self._save_todos()
                self._refresh_todo_list()
                break
    
    def _delete_todo(self, todo_id, widget):
        # Animation für das Löschen
        self._animate_fade_out(widget, lambda: self._perform_delete(todo_id))
    
    def _perform_delete(self, todo_id):
        self.todos = [todo for todo in self.todos if todo.id != todo_id]
        self._save_todos()
        self._refresh_todo_list()
    
    def _filter_todos(self, filter_type):
        self.current_filter = filter_type
        self._update_filter_buttons()
        self._refresh_todo_list()
    
    def _update_filter_buttons(self):
        for filter_type, button in self.filter_buttons.items():
            button.setProperty("active", filter_type == self.current_filter)
            button.style().unpolish(button)
            button.style().polish(button)
    
    def _refresh_todo_list(self):
        # Lösche alle vorhandenen Widgets
        while self.todo_list_layout.count():
            item = self.todo_list_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        # Filtere Todos
        filtered_todos = []
        if self.current_filter == "all":
            filtered_todos = self.todos
        elif self.current_filter == "active":
            filtered_todos = [todo for todo in self.todos if not todo.completed]
        elif self.current_filter == "completed":
            filtered_todos = [todo for todo in self.todos if todo.completed]
        
        # Füge gefilterte Todos hinzu
        for todo in filtered_todos:
            todo_widget = TodoWidget(todo, self)
            # Verbinde Signale
            todo_widget.toggled.connect(self._toggle_todo)
            todo_widget.edited.connect(self._edit_todo)
            todo_widget.deleted.connect(lambda id, widget=todo_widget: self._delete_todo(id, widget))
            
            self.todo_list_layout.addWidget(todo_widget)
    
    def _load_todos(self):
        try:
            if os.path.exists("todos.json"):
                with open("todos.json", "r") as f:
                    todos_data = json.load(f)
                    self.todos = [Todo.from_dict(todo_dict) for todo_dict in todos_data]
            self._refresh_todo_list()
        except Exception as e:
            print(f"Fehler beim Laden der Todos: {e}")
    
    def _save_todos(self):
        try:
            todos_data = [todo.to_dict() for todo in self.todos]
            with open("todos.json", "w") as f:
                json.dump(todos_data, f)
        except Exception as e:
            print(f"Fehler beim Speichern der Todos: {e}")
    
    def _animate_window_open(self):
        # Disable window opening animation for now
        pass
    
    def _animate_fade_in(self, widget, duration=300, callback=None):
        if not widget:
            return
            
        # Make sure widget is visible first
        widget.show()
        widget.setVisible(True)
        
        # Remove any existing effects
        widget.setGraphicsEffect(None)
        
        # Skip animation for now to debug layout
        return
        
        # Commented out animation code for debugging
        """
        # Erstelle einen Opacity-Effekt
        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
        effect.setOpacity(0)
        
        # Erstelle die Animation
        animation = QPropertyAnimation(effect, b"opacity")
        animation.setDuration(duration)
        animation.setStartValue(0)
        animation.setEndValue(1)
        animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        if callback:
            animation.finished.connect(callback)
            
        animation.start()
        """

    def _animate_fade_out(self, widget, callback=None, duration=300):
        if not widget:
            return
            
        # Just hide the widget for now
        widget.hide()
        if callback:
            callback()
            
        # Skip animation for now
        return
        
        # Commented out animation code for debugging
        """
        # Erstelle einen Opacity-Effekt
        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
        effect.setOpacity(1)
        
        # Erstelle die Animation
        animation = QPropertyAnimation(effect, b"opacity")
        animation.setDuration(duration)
        animation.setStartValue(1)
        animation.setEndValue(0)
        animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        if callback:
            animation.finished.connect(callback)
            
        animation.start()
        """