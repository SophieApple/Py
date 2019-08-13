import sys,requests,sip
# sys.path.append('D:\PycharmProjects\Py\FMStest\test')
from .UI import Ui_MianWIndow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui
import pandas as pd

class Show(QMainWindow,Ui_MianWIndow):
    def __init__(self):
        super(Show, self).__init__()
        self.setWindowIcon(QtGui.QIcon('./fms.png'))
        self.body_edit = QtWidgets.QTextEdit()
        self.body_edit.setPlaceholderText('输入Body')
        self.query_edit = QtWidgets.QTextEdit()
        self.query_edit.setPlaceholderText('输入Query')
        self.header_edit = QtWidgets.QTextEdit()
        self.header_edit.setPlaceholderText('输入Header')
        self.setupUi(self)
        self.setWindowTitle('FMS apitest')
        self.pushButton_in.clicked.connect(self.ImportExcel)
        self.comboBox_way.activated.connect(self.ChoicePath)
        self.pushButton_request.clicked.connect(self.Request)
        self.checkBox_body.stateChanged.connect(self.Body)
        self.checkBox_query.stateChanged.connect(self.Query)
        self.checkBox_header.stateChanged.connect(self.Header)

    def ImportExcel(self):

        self.filename,self.filetype = QFileDialog.getOpenFileName(self,"选择文件","./","所有文件 (*);;Excel (.xlsx)")
        try:
            self.list = pd.read_excel(self.filename).values
            for i in self.list:
                self.comboBox_way.addItem(i[0])
        except:
            print('未选择文件')

    def ChoicePath(self):
        self.path = self.list[self.comboBox_way.currentIndex()][2]
        self.method = self.list[self.comboBox_way.currentIndex()][1]
        self.label_method.setText(self.method)
        print(self.method,self.path)

    def Request(self):
        self.url = 'http://192.168.83.200:8088{}',format(self.path)


    def Body(self):
        if self.checkBox_body.isChecked():
            self.Layout_param.addWidget(self.body_edit)
        if not self.checkBox_body.isChecked():
            self.Layout_param.removeWidget(self.body_edit)
            sip.delete(self.body_edit)
            self.body_edit = QtWidgets.QTextEdit()
            self.body_edit.setPlaceholderText('输入Body')

    def Query(self):
        if self.checkBox_query.isChecked():
            self.Layout_param.addWidget(self.query_edit)
        if not self.checkBox_query.isChecked():
            self.Layout_param.removeWidget(self.query_edit)
            sip.delete(self.query_edit)
            self.query_edit = QtWidgets.QTextEdit()
            self.query_edit.setPlaceholderText('输入Query')

    def Header(self):
        if self.checkBox_header.isChecked():
            self.Layout_param.addWidget(self.header_edit)
        if not self.checkBox_header.isChecked():
            self.Layout_param.removeWidget(self.header_edit)
            sip.delete(self.header_edit)
            self.header_edit = QtWidgets.QTextEdit()
            self.header_edit.setPlaceholderText('输入Header')

    def Result(self):
        self.

def main():
    app = QApplication(sys.argv)
    gui = Show()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()