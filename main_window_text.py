import sys

from PyQt6.QtWidgets import(
    QApplication,
    QWidget,
    QLabel, 
    QMainWindow,
    QStatusBar,
    QToolBar
)

class Window(QMainWindow):
    def __init__(self):

        # create instance of Window Object
        super().__init__(parent=None)
        self.setWindowTitle("Main Window Test")
        self.setCentralWidget(QLabel("This is the Central Widget"))
        self._createMenu()
        self._createToolBar()   
        self._createStatusBar()

    
    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    
    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    
    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("This is the Status Bar")
        self.setStatusBar(status)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())