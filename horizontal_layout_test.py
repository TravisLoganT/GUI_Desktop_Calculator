import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

# create instance of application and window interface
app = QApplication([])
window = QWidget()
window.setWindowTitle("Horizontal Grid Test")

# create the buttons in the horizontal grid; present in correct layout
layout = QHBoxLayout()
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Right"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())