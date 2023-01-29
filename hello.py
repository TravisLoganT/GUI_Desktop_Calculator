import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle("Calculator")
window.setGeometry(200, 200, 300, 100)
helloMessage = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMessage.move(60, 15)

window.show()

sys.exit(app.exec())