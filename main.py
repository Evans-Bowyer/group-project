from PySide6 import QtCore as qt
from PySide6 import QtWidgets as wdgt
from PySide6 import QtGui as gui
import sys

class MyWidget(wdgt.QWidget):
    def __init__(self):
        super().__init__()

        self.button = wdgt.QPushButton("Confirm")
        self.text = wdgt.QLabel("Hello, World!", alignment=qt.Qt.AlignCenter)

        self.layout = wdgt.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.change_yr)

    @qt.Slot()
    def change_yr(self):
        self.text.setText("It works!")

#   def make_list(items, position): 
        

if __name__ == "__main__" :
    app = wdgt.QApplication([])

    widget = MyWidget()
    widget.resize(800,600)
    widget.show()

    sys.exit(app.exec())
