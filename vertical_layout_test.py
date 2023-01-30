import sys

from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget
)

# create an instance of the application and window configuration
app = QApplication([])
window = QWidget()
window.setWindowTitle("Vertical Box Test")

# Create the box Layout and insert the pressible buttons in the desired format
layout = QVBoxLayout()
layout.addWidget(QPushButton("Top"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Bottom"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())