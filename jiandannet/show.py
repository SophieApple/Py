from analyseimg import analyseUrl
from MainWindow import UI_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui,QtCore
import sys

class Test(UI_MainWindow):
    def __init__(self):
        super(Test, self).__init__()
        self.datalist = []

    def run(self):
        an = analyseUrl()
        for i in range(1,200):
            url = 'http://jandan.net/pic/page-{}#comments'.format(i)
            an.get(url=url)
            self.datalist.append(an.imglistb)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Test()
    gui.run()
    print(gui.datalist)
    gui.show()
    sys.exit(app.exec_())