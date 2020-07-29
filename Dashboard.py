# https://pythonspot.com/gui/
# https://pythonspot.com/pyqt5-tabs/
import sys
import pyautogui

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'RuneScape Killer'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()
# create a grid layout
def createGridLayout(self):
    self.horizontalGroupBox = QGroupBox("Grid")
    layout = QGridLayout()
    layout.setColumnStretch(1, 4)
    layout.setColumnStretch(2, 4)
# Grid widgets added using: layout.addWidget(Widget,X,Y), see https://pythonspot.com/pyqt5-grid-layout/

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(400, 500)

        # Add tabs
        self.tabs.addTab(self.tab1, "Setup")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Information")

        # Tab 1
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("Run Bot")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        # Tab 2
        self.tab2.layout = QVBoxLayout(self)
        self.pushButton2 = QPushButton("Run Bot")
        self.tab2.layout.addWidget(self.pushButton2)
        self.tab2.setLayout(self.tab2.layout)

        # Tab 3
        self.tab3.layout = QVBoxLayout(self)
        #self.pushButton3 = QPushButton("Run Bot")
        #self.tab3.layout.addWidget(self.pushButton3)
        #self.tab3.print(pyautogui.size())


        self.tab3.setLayout(self.tab3.layout)



        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())