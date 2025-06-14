from PySide6.QtWidgets import QHBoxLayout, QPushButton, QTableView, QLabel
from PySide6.QtSql import QSqlTableModel
from widgets.base_page import BasePage

class PartnersPage(BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.content_layout.addWidget(QLabel("Управление партнерами"))
        
        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Добавить")
        self.btn_edit = QPushButton("Редактировать")
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_edit)
        self.content_layout.addLayout(btn_layout)
        
        self.table = QTableView()
        self.model = QSqlTableModel()
        self.model.setTable("partners")
        self.table.setModel(self.model)
        self.content_layout.addWidget(self.table) 