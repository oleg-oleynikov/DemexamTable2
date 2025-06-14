from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QScrollArea, QHBoxLayout
from widgets.base_page import BasePage
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from db import db
from styles import COLORS

class MaterialsPage(BasePage):
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
        
        title = QLabel("Материалы")
        title.setStyleSheet("font-size: 18pt; font-weight: bold;")
        self.layout.addWidget(title)


        self.load_materials()

        scroll.setWidget(content)
        self.content_layout.addWidget(scroll)

    def load_materials(self):
        print("Начало загрузки материалов...")
        try:
            with db.conn.cursor() as cur:
                cur.execute("""
                    SELECT name, current_quantity, min_quantity, 
                           current_cost, unit, package_quantity
                    FROM materials
                    ORDER BY name
                """)
                materials = cur.fetchall()
                print(f"Получено {len(materials)} записей из БД")
                
                if not materials:
                    print("Внимание: материалы не найдены!")
                    empty_label = QLabel("Нет данных о материалах")
                    empty_label.setStyleSheet("color: red; font-size: 16pt;")
                    self.layout.addWidget(empty_label)
                    return
                
                for material in materials:
                    print(f"Обработка материала: {material[0]}")
                    self.add_material_card(*material)
        except Exception as e:
            print(f"Ошибка: {str(e)}")
            self.main_window.show_error("Ошибка", f"Не удалось загрузить материалы:\n{str(e)}")

    def add_material_card(self, name, current_qty, min_qty, price, unit, package_quantity):
        print(f"Добавление карточки: {name}")
        
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
        name_label = QLabel(f"<b>Материал:</b> {name}")
        layout.addWidget(name_label)
        qty_label = QLabel(f"<b>Количество на складе:</b> {current_qty}")
        layout.addWidget(qty_label)
        min_label = QLabel(f"<b>Мин. количество:</b> {min_qty}")
        layout.addWidget(min_label)
        quantityPackage = QLabel(f"<b> Количество в упаковке: </b> {package_quantity}")
        layout.addWidget(quantityPackage)
        price_label = QLabel(f"<b>Цена:</b> {price:.2f} руб")
        layout.addWidget(price_label)
        unit_label = QLabel(f"<b>Ед. изм.:</b> {unit}")
        layout.addWidget(unit_label)
        self.layout.addWidget(card)
        print(f"Карточка '{name}' добавлена в макет")