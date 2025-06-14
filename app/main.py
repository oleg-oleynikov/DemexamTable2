from PySide6.QtWidgets import QApplication
from app import MainWindow
from PySide6.QtGui import QFontDatabase
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if "Gabriola" not in QFontDatabase().families():
        print("Шрифт Gabriola не найден! Установите его в систему")
        sys.exit(1)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())