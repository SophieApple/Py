from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui
import sys
import pandas as pd

class UI_MainWindow(QMainWindow):
    def __init__(self):
        super(UI_MainWindow, self).__init__()
        self.setWindowTitle('FMSApitest')
        self.setWindowIcon(QtGui.QIcon('./fms.png'))
        self.resize(640,480)
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)
        # self.pushbutton_add = QtWidgets.QPushButton()
        # self.main_layout.addWidget(self.pushbutton_add)
        # self.pushbutton_add.setText('加一行')
        self.setCentralWidget(self.main_widget)
        # self.pushbutton_add.clicked.connect(self.Addline)
        self.combox = QtWidgets.QComboBox()
        self.methodlebal = QtWidgets.QLabel()
        self.combox.activated.connect(self.Label)

    def Addline(self):
        self.lineedit = QLineEdit()
        self.main_layout.addWidget(self.lineedit)

    def Getexcel(self):
        excel = pd.read_excel('./FMS接口.xlsx')
        self.lines = excel.values
        for i in self.lines:
            self.combox.addItem(i[0],i[1])
        self.main_layout.addWidget(self.combox)

    def Label(self):
        self.methodlebal.setText(str(self.lines[self.combox.currentIndex()][1]))
        self.main_layout.addWidget(self.methodlebal)


def main():
    app = QApplication(sys.argv)
    gui = UI_MainWindow()
    gui.Getexcel()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()