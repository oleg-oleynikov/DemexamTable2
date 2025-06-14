from PySide6.QtWidgets import QMainWindow, QStackedWidget, QMessageBox
from widgets.navigation import NavigationBar
from widgets.home_page import HomePage
from widgets.partners_page import PartnersPage
from widgets.products_page import ProductsPage
from widgets.materials_page import MaterialsPage
from collections import deque  
from styles import COLORS, setup_fonts, LOGO_PATH, APP_ICON_PATH
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__() 

        self.setWindowTitle("Управление компанией")
        self.setWindowIcon(QIcon(APP_ICON_PATH))
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {COLORS["primary_bg"]};
            }}
            QToolBar {{
                background-color: {COLORS["secondary_bg"]};
                border: none;
                padding: 5px;
            }}
        """)
        self.resize(1024, 768)
        
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        
        self.pages = {
            "home": HomePage(self),
            "partners": PartnersPage(self),
            "products": ProductsPage(self),
            "materials": MaterialsPage(self)
        }
        
        for page in self.pages.values():
            self.central_widget.addWidget(page)
        
        self.nav_bar = NavigationBar(self)
        self.addToolBar(self.nav_bar)
        
        self.nav_bar.materials_clicked.connect(lambda: self.switch_page("materials"))
        self.nav_bar.home_clicked.connect(lambda: self.switch_page("home"))
        self.nav_bar.partners_clicked.connect(lambda: self.switch_page("partners"))
        self.nav_bar.products_clicked.connect(lambda: self.switch_page("products"))
       
        self.history = deque(maxlen=10)
    
    def switch_page(self, page_name, add_to_history=True):
        if add_to_history:
            current_page = self.central_widget.currentWidget()
            if current_page:
                self.history.append(current_page)
        self.central_widget.setCurrentWidget(self.pages[page_name])

    def go_back(self):
        if self.history:
            prev_page = self.history.pop()
            self.central_widget.setCurrentWidget(prev_page)

    def show_error(self, title, message):
        QMessageBox.critical(
            self,
            title,
            message,
            QMessageBox.StandardButton.Ok
        )