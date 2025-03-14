STYLES = """
/* Allgemeine Stile */
QWidget {
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 12px;
    color: #333333;
    background-color: #ffffff;
    opacity: 1;
}

/* Scroll Area */
QScrollArea {
    border: none;
    background-color: transparent;
}

QScrollArea > QWidget > QWidget {
    background-color: transparent;
}

QScrollBar:vertical {
    border: none;
    background: #f0f0f0;
    width: 10px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background: #c0c0c0;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background: #a0a0a0;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

/* Todo Container */
#todo-container {
    background-color: transparent;
    border: none;
    margin: 10px 0;
}

#page-scroll {
    background-color: transparent;
}

/* Navbar */
#navbar {
    background-color: #ffffff;
    border-bottom: 1px solid #e0e0e0;
    padding: 10px;
    min-height: 50px;
    opacity: 1;
}

#logo {
    font-size: 18px;
    font-weight: bold;
    color: #3b82f6;
}

#nav-button {
    background-color: transparent;
    border: none;
    color: #666666;
    padding: 8px 12px;
    border-radius: 4px;
}

#nav-button:hover {
    background-color: #f0f0f0;
    color: #3b82f6;
}

/* Hero Section */
#hero-frame {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ebf5ff, stop:1 #ffffff);
    border-radius: 8px;
    padding: 40px;
    margin: 20px 0;
    opacity: 1;
}

#hero-title {
    font-size: 32px;
    font-weight: bold;
    color: #3b82f6;
    margin-bottom: 10px;
    opacity: 1;
}

#hero-subtitle {
    font-size: 16px;
    color: #666666;
    margin-bottom: 20px;
    opacity: 1;
}

#cta-button {
    background-color: #3b82f6;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 10px 20px;
    font-weight: bold;
}

#cta-button:hover {
    background-color: #2563eb;
}

/* Feature Cards */
#feature-card {
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    margin: 10px;
    opacity: 1;
}

#feature-card:hover {
    border-color: #3b82f6;
}

#feature-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
}

#feature-desc {
    color: #666666;
}

/* Page Titles */
#page-title {
    font-size: 28px;
    font-weight: bold;
    color: #3b82f6;
    margin-bottom: 10px;
}

#page-subtitle {
    font-size: 16px;
    color: #666666;
    margin-bottom: 30px;
}

/* Todo Input */
#todo-input {
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    padding: 10px;
    font-size: 14px;
}

#todo-input:focus {
    border-color: #3b82f6;
    outline: none;
}

#add-button {
    background-color: #3b82f6;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 10px 15px;
    font-weight: bold;
}

#add-button:hover {
    background-color: #2563eb;
}

/* Filter Buttons */
#filter-button {
    background-color: transparent;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    padding: 8px 15px;
    margin: 0 5px;
}

#filter-button:hover {
    background-color: #f0f0f0;
}

#filter-button[active="true"] {
    background-color: #3b82f6;
    color: white;
    border-color: #3b82f6;
}

/* Todo List */
#todo-list-scroll {
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    background-color: #f9f9f9;
    opacity: 1;
}

#todo-item {
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    margin: 5px;
    padding: 10px;
    opacity: 1;
}

#todo-item:hover {
    border-color: #3b82f6;
}

#todo-item[completed="true"] {
    background-color: #f0f0f0;
}

#todo-text {
    font-size: 14px;
}

#todo-edit {
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    padding: 5px;
}

#edit-button, #save-button, #cancel-button, #delete-button {
    background-color: transparent;
    border: none;
    border-radius: 4px;
    padding: 5px 10px;
}

#edit-button {
    color: #3b82f6;
}

#save-button {
    color: #10b981;
}

#cancel-button {
    color: #6b7280;
}

#delete-button {
    color: #ef4444;
}

#edit-button:hover, #save-button:hover, #cancel-button:hover, #delete-button:hover {
    background-color: #f0f0f0;
}

/* About Page */
#content-section {
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    opacity: 1;
}

#section-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 15px;
}

#section-text {
    color: #666666;
    margin-bottom: 10px;
    line-height: 1.5;
}

#team-member {
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    margin: 10px;
}

#member-name {
    font-size: 18px;
    font-weight: bold;
}

#member-role {
    color: #666666;
    font-style: italic;
    margin-bottom: 10px;
}

#member-desc {
    color: #666666;
}

/* Contact Page */
#contact-info, #contact-form {
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    margin: 10px;
    opacity: 1;
}

#contact-label {
    font-weight: bold;
    margin-bottom: 5px;
}

#contact-value {
    color: #666666;
    margin-bottom: 15px;
}

#form-label {
    font-weight: bold;
    margin-bottom: 5px;
}

#form-input {
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    padding: 10px;
    margin-bottom: 10px;
}

#submit-button {
    background-color: #3b82f6;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 10px 15px;
    font-weight: bold;
    width: 100%;
}

#submit-button:hover {
    background-color: #2563eb;
}

/* Footer */
#footer {
    background-color: #ffffff;
    border-top: 1px solid #e0e0e0;
    padding: 10px;
    min-height: 50px;
    opacity: 1;
}

#copyright {
    color: #666666;
}

#social-button {
    background-color: transparent;
    border: none;
    color: #666666;
    padding: 5px 10px;
}

#social-button:hover {
    color: #3b82f6;
}
"""