import sys,requests
# sys.path.append('D:\PycharmProjects\Py\FMStest\test')
from UI import Ui_MianWIndow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui

class Show(QMainWindow,Ui_MianWIndow):
    def __init__(self):
        super(Show, self).__init__()
        self.setupUi(self)
        self.pushButton_in.clicked.connect(self.ImportExcel)


    def ImportExcel(self):

        self.filename,self.filetype = QFileDialog.getOpenFileName(self,"选择文件","./","所有文件 (*);;Excel (.xlsx)")
        print(self.filename)
        print(self.filetype)


def main():
    app = QApplication(sys.argv)
    gui = Show()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()