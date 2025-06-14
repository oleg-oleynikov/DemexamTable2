from PySide6.QtWidgets import QToolBar
from PySide6.QtCore import Signal

class NavigationBar(QToolBar):
    home_clicked = Signal()
    partners_clicked = Signal()
    products_clicked = Signal()
    materials_clicked = Signal()
    
    def __init__(self, parent=None):
        super().__init__("Навигация", parent)
        self.addAction("Главная", self.home_clicked.emit)
        self.addAction("Продукция", self.products_clicked.emit)
        self.addAction("Партнеры", self.partners_clicked.emit)
        self.addAction("Материалы", self.materials_clicked.emit)
        self.addAction("Выход", parent.close)