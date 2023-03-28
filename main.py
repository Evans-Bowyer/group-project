from PySide6 import QtCore as qt
from PySide6 import QtWidgets as wdgt
from PySide6 import QtGui as gui
import sys

class MyWidget(wdgt.QWidget):
    def __init__(self):
        super().__init__()

        years = ["2013", "2014", "2015", "2016",
                "2017", "2018", "2019", "2020"]
        pollutants = [

        # define menu to select chemical to show data for
        self.chem_menu = wdgt.QComboBox()

        # define menu to select year to show
        self.year_menu = wdgt.QComboBox()
        self.year_menu.addItems(years)
        # TODO: figure out how to manipulate size and position of widgets

        # button to confirm choice and reload map
        self.button = wdgt.QPushButton("Confirm")

        # add widgets to display
        self.layout = wdgt.QVBoxLayout(self)
        self.layout.addWidget(self.year_menu)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.reload_display)

    @qt.Slot()
    def reload_display(self):
        #TODO: write function to reload data on button press
        self.text.setText("It works!")

if __name__ == "__main__" :
    app = wdgt.QApplication([])

    widget = MyWidget()
    widget.resize(800,600)
    widget.show()

    sys.exit(app.exec())
