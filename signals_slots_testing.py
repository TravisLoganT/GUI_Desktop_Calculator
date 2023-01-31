import sys
from functools import partial

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton, 
    QVBoxLayout,
    QWidget
)


def greet(name):
    # create the chosen text that will be used to greet
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText(f"Hello, {name}!")


# set up the instance of the application
app = QApplication([])
window = QWidget()
window.setWindowTitle("Signals and Slots Testing")
layout = QVBoxLayout()

# create the button to give the greeting
button = QPushButton("Greet")
button.clicked.connect(partial(greet, "Travis"))

# Add the Widgets and create the 
layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())