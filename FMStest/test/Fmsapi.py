import sys,requests,sip
# sys.path.append('D:\PycharmProjects\Py\FMStest\test')
from UI import Ui_MianWIndow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui
import pandas as pd

class Show(QMainWindow,Ui_MianWIndow):
    def __init__(self):
        super(Show, self).__init__()
        self.setWindowIcon(QtGui.QIcon('./fms.png'))
        self.body_edit = QtWidgets.QTextEdit()
        self.setupUi(self)
        self.pushButton_in.clicked.connect(self.ImportExcel)
        self.comboBox_way.activated.connect(self.ChoicePath)
        self.pushButton_request.clicked.connect(self.Request)
        self.checkBox_body.stateChanged.connect(self.Body)

    def ImportExcel(self):

        self.filename,self.filetype = QFileDialog.getOpenFileName(self,"选择文件","./","所有文件 (*);;Excel (.xlsx)")
        print(self.filename)
        print(self.filetype)
        self.list = pd.read_excel(self.filename).values
        for i in self.list:
            self.comboBox_way.addItem(i[0])

    def ChoicePath(self):
        self.path = self.list[self.comboBox_way.currentIndex()][2]
        self.method = self.list[self.comboBox_way.currentIndex()][1]
        print(self.method,self.path)

    def Request(self):
        self.url = 'http://192.168.83.200:8088{}',format(self.path)


    def Body(self):
        if self.checkBox_body.isChecked():
            self.Layout_param.addWidget(self.body_edit)
        if not self.checkBox_body.isChecked():
            self.Layout_param.removeWidget(self.body_edit)
            sip.delete(self.body_edit)
            print('remove')
            # self.body_edit = QtWidgets.QTextEdit()


def main():
    app = QApplication(sys.argv)
    gui = Show()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()