from PySide6.QtGui import QFont

# Шрифты
def setup_fonts():
    font = QFont("Gabriola")
    font.setPointSize(12)
    return font

# Цвета
COLORS = {
    "primary_bg": "#FFFFFF",
    "secondary_bg": "#BBD9B2",  
    "accent": "#2D6033",  
    "text": "#000000"
}

LOGO_PATH = "resources/Наш декор.png"
APP_ICON_PATH = "resources/Наш декор.ico"