from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QScrollArea, QHBoxLayout
from widgets.base_page import BasePage
from PySide6.QtCore import Qt
from db import db
from styles import COLORS

class ProductsPage(BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title = QLabel("Каталог продукции")
        self.title.setStyleSheet("""
            font-size: 20pt;
            font-weight: bold;
            color: #2D6033;
            margin: 10px;
        """)
        if not db.conn:
            self.show_error("Нет подключения к БД")
            return
        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)
        layout.addWidget(self.title, alignment=Qt.AlignCenter)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        
        content = QWidget()
        self.layout = QVBoxLayout(content)
        
        title = QLabel("Каталог продукции")
        title.setStyleSheet("font-size: 18pt; font-weight: bold;")
        self.layout.addWidget(title)

        self.load_products()

        scroll.setWidget(content)
        self.content_layout.addWidget(scroll)

    def load_products(self):
        products = db.get_products()
        for product in products:
            self.add_product_card(*product)

    def add_product_card(self, article, name, partner_price, product_type, width, price):
        card = QFrame()
        card.setFrameShape(QFrame.StyledPanel)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: #BBD9B2;
                border-radius: 8px;
                margin: 10px;
            }}
            QLabel {{
                color: {COLORS["text"]};
                font-size: 18px;
                margin: 2px;
                border: 0px;
            }}
        """)

        layout = QVBoxLayout(card)

        row1 = QHBoxLayout()
        row1.addWidget(QLabel(f"<b>Тип:</b> {product_type}"))
        row1.addStretch()
        row1.addWidget(QLabel(f"<b>Наименование:</b> {name}"))
        row1.addStretch()
        row1.addWidget(QLabel(f"<b>Стоимость:</b> {price} р"))
        layout.addLayout(row1)
        layout.addWidget(QLabel(f"<b>Артикул:</b> {article}"))
        layout.addWidget(QLabel(f"<b>Мин. стоимость для партнера:</b> {partner_price} р"))
        layout.addWidget(QLabel(f"<b>Ширина:</b> {width} м"))

        self.layout.addWidget(card)