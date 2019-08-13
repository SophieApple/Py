import sys,requests,sip,json
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
        self.pushButton_clear.clicked.connect(self.Clear)
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
        self.name = self.comboBox_way.currentText()
        self.path = self.list[self.comboBox_way.currentIndex()][2]
        self.method = self.list[self.comboBox_way.currentIndex()][1]
        self.label_method.setText(self.method)
        self.lineEdit_path.setText(self.path)
        print(self.method,self.path)


    def Request(self):
        print('in')
        self.request_body = ''
        self.request_header = ''
        self.request_query = ''
        # self.truepath = self.lineEdit_path.text()
        Mark = True
        self.url = 'http://192.168.83.200:8088{}'.format(self.lineEdit_path.text())
        if self.checkBox_body.isChecked() and len(self.body_edit.toPlainText()) != 0:
            try:
                self.request_body = json.loads(self.body_edit.toPlainText())
                print(self.request_body)
            except Exception as e:
                print(e)
                Mark = False
        if self.checkBox_header.isChecked() and len(self.header_edit.toPlainText()) != 0:
            try:
                self.request_header = json.loads(self.header_edit.toPlainText())
            except Exception as e:
                print(e)
                Mark = False
        if self.checkBox_query.isChecked() and len(self.query_edit.toPlainText()) != 0:
            try:
                self.request_query = json.loads(self.query_edit.toPlainText())
            except Exception as e:
                print(e)
                Mark = False
        print('here')
        print(self.method,self.url)
        if Mark:
            response = requests.request(method=self.method,url=self.url,params=self.request_query,headers=self.request_header,data=self.request_body)
            print(response.content)
            # self.Result('{}:\t{}'.format(self.name,response.status_code))
            self.Result(response.text)
            # self.Result(str(response.status_code))


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

    def Result(self,list):
        self.textBrowser_result.append(list)
        # self.textBrowser_result.setText(list)

    def Clear(self):
        self.textBrowser_result.setText("")


def main():
    app = QApplication(sys.argv)
    gui = Show()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()