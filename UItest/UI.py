from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import *
import sys
from untitled import Ui_Form

class Show(QMainWindow,Ui_Form):
    def __init__(self):
        super(Show, self).__init__()
        self.setupUi(self)
        self.dial.valueChanged.connect(self.lcd)
    def lcd(self):
        self.lcdNumber.display(str(self.dial.value()))
        print(str(self.dial.value()))

def main():
    app = QApplication(sys.argv)
    gui = Show()
    print(gui.dial.show)
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
