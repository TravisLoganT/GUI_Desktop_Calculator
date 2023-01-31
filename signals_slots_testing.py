import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton, 
    QVBoxLayout,
    QWidget
)


def greet():
    # create the chosen text that will be used to greet
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText("Hello World!")


# set up the instance of the application
app = QApplication([])
window = QWidget()
window.setWindowTitle("Signals and Slots Testing")
layout = QVBoxLayout()

# create the button to give the greeting
button = QPushButton("Greet")
button.clicked.connect(greet)

# Add the Widgets and create the 
layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())