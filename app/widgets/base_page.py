from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtSql import QSqlDatabase
from PySide6.QtCore import Qt
from styles import COLORS

class BasePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {COLORS["primary_bg"]};
                font-family: Gabriola;
                color: black;
            }}
        """)
        self.main_window = parent
        
        self.main_layout = QVBoxLayout(self)
        
        self.content_layout = QVBoxLayout()
        self.main_layout.addLayout(self.content_layout)
    
        self.btn_back = QPushButton("← Назад")
        self.btn_back.setStyleSheet(f"""
           QWidget {{
                background-color: {COLORS["secondary_bg"]};
                font-family: Gabriola;
            }} 
        """)
        self.btn_back.setFixedSize(100, 30)
        self.btn_back.clicked.connect(self.go_back)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.btn_back, 0, Qt.AlignRight)
        
    def go_back(self):
        if self.main_window:
            self.main_window.go_back()

    def check_database_connection(self):
        if not QSqlDatabase.database().isOpen():
            if hasattr(self.main_window, 'show_error'):
                self.main_window.show_error(
                    "Ошибка БД",
                    "Нет подключения к базе данных. Закройте программу и проверьте соединение."
                )
            return False
        return True