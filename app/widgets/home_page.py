from PySide6.QtWidgets import QLabel, QVBoxLayout
from widgets.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        label = QLabel("Добро пожаловать в систему управления!")
        label.setStyleSheet(f"""QLabel{{font-size:20px;}}""")
        self.content_layout.addWidget(label)
        self.btn_back.hide()