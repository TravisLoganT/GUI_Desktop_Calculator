import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

SIZE_OF_WINDOW = 235


class CalculatorWindow(QMainWindow):
    """The Calculator's main application window (GUI)"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(SIZE_OF_WINDOW, SIZE_OF_WINDOW)
        centerWidget = QWidget(self)
        self.setCentralWidget(centerWidget)

def main():
    """Calculators Main Function Control"""
    calculatorApp = QApplication([])
    calculatorWindow = CalculatorWindow()
    calculatorWindow.show()
    sys.exit(calculatorApp.exec())


if __name__ == "__main__":
    main()
