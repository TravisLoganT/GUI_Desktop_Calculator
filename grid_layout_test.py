import sys

from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget
)

# create instance of application and window configuration
app = QApplication([])
window = QWidget()
window.setWindowTitle("Grid Layout Test")

# create basis for grid layout
layout = QGridLayout()

# first button row from left to right
layout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
layout.addWidget(QPushButton("Button (0, 2)"), 0, 2)

# second button row from left to right
layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
layout.addWidget(QPushButton("Button (1, 2)"), 1, 2)

# third button row from left to right + a button that spans 2 columns
layout.addWidget(QPushButton("Button (2, 0)"), 2, 0)
layout.addWidget(QPushButton("Button (2, 1) + 2 Columns Span)"), 2, 1, 1, 2)

window.setLayout(layout)

window.show()
sys.exit(app.exec())



