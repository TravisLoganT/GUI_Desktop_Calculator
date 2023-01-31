import sys

from PyQt6.QtWidgets import (
    QApplication, 
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout
)

class Window(QDialog):
    # create the instance of the Window
    def __init__(self):
        super().__init__(parent=None)

        # create the window object and it's form structure
        self.setWindowTitle("Dialog Box Test")
        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()

        # add the dialog boxes
        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Number:", QLineEdit())
        dialogLayout.addLayout(formLayout)

        # create the actionable buttons
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel |
             QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
