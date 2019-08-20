import sys, requests, sip, json,configparser,time,random
# sys.path.append('D:\PycharmProjects\Py\FMStest\test')
from UI import Ui_MianWIndow

try:
    from .UI import Ui_MianWIndow
except:
    print()
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import pandas as pd
import logging

host = 'http://192.168.83.200:8088'
# headers = '{"token":"ZGV2LDE1NjgxNjgzOTM1NDEsZWFmOTU1MTRkYTQyM2Y2MTE3OTRkYjg5MTUzMmFiNDY="}'
headers = '{"token":"ZGV2LDE1NjgxNjgzOTM1NDEsZWFmOTU1MTRkYTQyM2Y2MTE3OTRkYjg5MTUzMmFiNDY="}'

logging.basicConfig(filename='test.log', filemode='a', format="%(asctime)s %(name)s:%(levelname)s:%(message)s",datefmt="%d-%M-%Y %H:%M:%S", level=logging.NOTSET)


class NewThread(QtCore.QThread):
    trigget = QtCore.pyqtSignal(dict)
    def __init__(self):
        super(NewThread, self).__init__()
        self.vehicles_Massage = {}
    def run(self):
        while True:
            # self.vehicles_Massage['vehicles_id'] = []
            # re = requests.get(url='http://192.168.83.200:8088/api/vehicles',headers={"cookie":'username=2|1:0|10:1565933869|8:username|4:ZGV2|1a8418e48b008340cf53d338f3085098f1349003a4a984c03b65e7280d47fc9e; userid="2|1:0|10:1565933869|6:userid|4:Mg==|c96070cf9ea41a922930b4d9340be76ab2e053634326689d4de847679d906ddc"'})
            #
            # # re = requests.get(url='http://192.168.83.200:8088/api/vehicles',headers={"token":"ZGV2LDE1NjgxNjgzOTM1NDEsZWFmOTU1MTRkYTQyM2Y2MTE3OTRkYjg5MTUzMmFiNDY="})
            # for i in json.loads(re.text)['vehicles']:
            #     self.vehicles_Massage['vehicles_id'].append(i['id'])
            # self.trigget.emit(self.vehicles_Massage)
            # print(self.vehicles_Massage)
            time.sleep(1)


class Show(QMainWindow, Ui_MianWIndow):
    def __init__(self):
        super(Show, self).__init__()

        self.setWindowIcon(QtGui.QIcon('./fms.png'))

        self.body_edit = QtWidgets.QPlainTextEdit()
        # self.body_edit = QtWidgets.QTextEdit()
        self.body_edit.setPlaceholderText('输入Body')
        self.query_edit = QtWidgets.QPlainTextEdit()
        # self.query_edit = QtWidgets.QTextEdit()
        self.query_edit.setPlaceholderText('输入Query')
        self.header_edit = QtWidgets.QPlainTextEdit()
        # self.header_edit = QtWidgets.QTextEdit()
        self.header_edit.setPlaceholderText('输入Header')

        self.setupUi(self)
        self.setWindowTitle('FMS apitest')
        self.pushButton_in.clicked.connect(self.ImportExcel)
        self.comboBox_way.activated.connect(self.ChoicePath)
        self.pushButton_request.clicked.connect(self.Request)
        self.pushButton_requestall.clicked.connect(self.RequestAll)
        self.pushButton_clear.clicked.connect(self.Clear)
        self.checkBox_body.stateChanged.connect(self.Body)
        self.checkBox_query.stateChanged.connect(self.Query)
        self.checkBox_header.stateChanged.connect(self.Header)
        self.pushButton_save.clicked.connect(self.Save)
        self.pushButton_saveAll.clicked.connect(self.SaveAll)
        self.pushButton_export.clicked.connect(self.Export)
        self.getvehicles_massage = NewThread()
        self.getvehicles_massage.trigget.connect(self.GetVehiclesMsg)
        self.getvehicles_massage.start()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Label_init)
        self.timer.start(3000)

        self.ImportExcel_init()


    def GetVehiclesMsg(self,Vehiclesiddict):
        """

        :param Vehiclesidlist:
        :return:dict
        """
        self.Vehiclesiddict = Vehiclesiddict
        # print(self.Vehiclesiddict)
        return self.Vehiclesiddict


    def Label_init(self):
        self.label_requeststatus.setText('')

    def Save(self):
        print('a')
        self.excelchange = pd.read_excel(self.filename)
        print('b')
        print(self.excelchange)
        # print(self.lineEdit_path.text(),self.header_edit.toPlainText(),self.query_edit.toPlainText(),self.body_edit.toPlainText())
        print(type(self.lineEdit_path.text()))
        try:
            self.excelchange['path'][self.comboBox_way.currentIndex()] = self.lineEdit_path.text()
        except Exception as e:
            logging.exception(e)
        try:
            self.excelchange['headers'][self.comboBox_way.currentIndex()] = self.header_edit.toPlainText()
        except Exception as e:
            logging.exception(e)
        try:
            self.excelchange['params'][self.comboBox_way.currentIndex()] = self.query_edit.toPlainText()
        except Exception as e:
            logging.exception(e)
        try:
            self.excelchange['body'][self.comboBox_way.currentIndex()] = self.body_edit.toPlainText()
        except Exception as e:
            logging.exception(e)
        print('done!')
        self.list = self.excelchange

        print('Save Success!!')

    def SaveAll(self):
        try:
            self.excelchange.to_excel(self.filename, index=False, header=True)
            print('SaveAll!!')
        except Exception as e:
            logging.exception(e)

    def ImportExcel_init(self):
        try:
            self.filename = './FMS接口.xlsx'
            self.comboBox_way.clear()
            self.list = pd.read_excel(self.filename)
            for i in self.list.values:
                self.comboBox_way.addItem(i[0])
            self.label_method.setText(self.list.values[self.comboBox_way.currentIndex()][1])
            self.lineEdit_path.setText(self.list.values[self.comboBox_way.currentIndex()][2])
        except Exception as e:
            print(e)

    def ImportExcel(self):

        self.filename, self.filetype = QFileDialog.getOpenFileName(self, "选择文件", "./", "所有文件 (*);;Excel (.xlsx)")
        try:
            self.comboBox_way.clear()
            self.list = pd.read_excel(self.filename)
            for i in self.list.values:
                self.comboBox_way.addItem(i[0])
            self.label_method.setText(self.list.values[self.comboBox_way.currentIndex()][1])
            self.lineEdit_path.setText(self.list.values[self.comboBox_way.currentIndex()][2])
        except:
            print('未选择文件或文件内容不符合规范')

    def ChoicePath(self):
        self.name = self.comboBox_way.currentText()
        self.path = self.list.values[self.comboBox_way.currentIndex()][2]
        self.method = self.list.values[self.comboBox_way.currentIndex()][1]
        self.label_method.setText(self.method)
        if self.method == 'GET':
            self.checkBox_body.setChecked(False)
            self.checkBox_body.setCheckable(False)
            self.Body()
        else:
            self.checkBox_body.setCheckable(True)
            self.Body()
        self.lineEdit_path.setText(self.path)
        print(self.method, self.path)

    def Request(self):
        print('in')
        self.method = self.label_method.text()
        self.name = self.comboBox_way.currentText()
        self.request_body = ''
        self.request_header = ''
        self.request_query = ''
        # self.truepath = self.lineEdit_path.text()
        Mark = True
        self.url = 'http://192.168.83.200:8088{}'.format(self.lineEdit_path.text())
        if self.checkBox_body.isChecked() and len(self.body_edit.toPlainText()) != 0:
            try:
                self.request_body = json.loads(self.ReplaceStr(s=self.body_edit.toPlainText()))
                # self.request_body = {"ip_addr": "10.22.52.211", "nickname": "testtest4", "mac_addr": ""}
                # print(self.request_body)
            except Exception as e:
                logging.exception(e)
                print(e)
                Mark = False
        if self.checkBox_header.isChecked() and len(self.header_edit.toPlainText()) != 0:
            try:
                self.request_header = json.loads(self.ReplaceStr(s=self.header_edit.toPlainText()))
            except Exception as e:
                logging.exception(e)
                Mark = False
        if self.checkBox_query.isChecked() and len(self.query_edit.toPlainText()) != 0:
            try:
                self.request_query = json.loads(self.ReplaceStr(s=self.query_edit.toPlainText()))
            except Exception as e:
                logging.exception(e)
                Mark = False
        # print('here')
        self.url = self.ReplaceStr(self.url)
        print(self.method, self.url)
        if not Mark:
            self.label_requeststatus.setText('请检查输入的参数！！')
            self.label_requeststatus.setStyleSheet('color: rgb(255, 0, 0)')
        if Mark:
            try:
                logging.debug('【Request】 [url]:{} [method]:{} [header]:{} [query]:{} [body]:{}'.format(self.url,self.method,self.request_header,self.request_query,self.request_body))
                response = requests.request(method=self.method, url=self.url, params=self.request_query,
                                            headers=self.request_header, json=self.request_body)
                self.label_requeststatus.setText('请求成功！')
                self.label_requeststatus.setStyleSheet('color: rgb(0,255,0)')
                print(response.text)
                # self.Result('{}:\t{}'.format(self.name,response.status_code))
                # self.Result(response.text)
                self.Result("{}\t{}".format(self.name, str(response.status_code)))
                self.ResponseBody(response.text)
            except Exception as e:
                logging.exception(e)
                self.label_requeststatus.setText('请求失败！')
                self.label_requeststatus.setStyleSheet('color: rgb(255, 0, 0)')

    def RequestAll(self):
        print('in')
        Len = len(self.list)
        print(Len)
        self.response_code = []
        self.response_text = []
        header = ''
        param = ''
        body = ''
        for i in range(0, Len):
            print('start')
            method = self.list['method'][i]
            url = "{}{}".format(host, self.list['path'][i])
            print(url)
            Mark = True
            if not self.list['headers'].isnull()[i]:
                try:
                    header = json.loads(self.list['headers'][i])
                    print(header)
                except Exception as e:
                    logging.exception(e)
                    Mark = False
            if not self.list['params'].isnull()[i]:
                try:
                    param = json.loads(self.list['params'][i])
                    print(param)
                except Exception as e:
                    logging.exception(e)
                    Mark = False

            if not self.list['body'].isnull()[i]:
                try:
                    body = json.loads(self.list['body'][i])
                    print(body)
                except Exception as e:
                    logging.exception(e)
                    Mark = False

            if Mark:
                print('start request!!!')
                logging.debug('【Request】 [url]:{} [method]:{} [header]:{} [query]:{} [body]:{}'.format(url,method,header,param,body))
                response = requests.request(method=method, url=url, headers=header, params=param, json=body)

                self.response_code.append(response.status_code)
                self.response_text.append(response.text)
                self.Result("{}\t{}".format(self.list['功能'][i], str(response.status_code)))
                print('request end\n')
            # except Exception as e:
            #     logging.exception(e)

        pass

    def Body(self):
        if self.checkBox_body.isChecked():
            self.Layout_param.addWidget(self.body_edit)
            if self.list['body'].isnull()[self.comboBox_way.currentIndex()]:
                self.body_edit.setPlainText('')
            else:
                self.body_edit.setPlainText(self.list['body'][self.comboBox_way.currentIndex()])
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
            try:
                self.header_edit.setPlainText(self.list['headers'][self.comboBox_way.currentIndex()])
            except Exception as e:
                logging.exception(e)
        if not self.checkBox_header.isChecked():
            self.Layout_param.removeWidget(self.header_edit)
            sip.delete(self.header_edit)
            self.header_edit = QtWidgets.QTextEdit()
            self.header_edit.setPlaceholderText('输入Header')

    def Result(self, list):
        self.textBrowser_result.append(list)
        # self.textBrowser_result.setText(list)

    def ResponseBody(self, list):
        self.textBrowser_responsebody.setText(list)
        # self.textBrowser_responsebody.setText(str(json.dumps(list,indent=2,ensure_ascii=False)))

    def Clear(self):
        self.textBrowser_result.setText("")

    def Export(self):
        resultList = self.textBrowser_result.toPlainText()
        self.ExportResult()
        if self.savepath != '':
            with open(self.savepath, 'w') as f:
                f.write(str(resultList))

    def ExportResult(self):
        self.savepath, self.savetype = QFileDialog.getSaveFileName(self, '选择保存路径', './', "All Files(*)")
        if self.savepath == '':
            print('取消选择')
            return
        print('\n保存文件：')
        print(self.savepath)
        print('类型：', self.savetype)

    def ReplaceStr(self,s):
        # if section in self.Secs:
        #     print('start')
        #     list = self.config.items(section)
        #     print(type(list))
            # for i in list:
            #     if i[1] == 'time':
            #         new = str(time.time()).split('.')[0][8:] + str(time.time()).split('.')[1][2:]
            #         s = s.replace(i[0],new)
            #         print('time')
            #     if i[1] == 'RandomIP':
            #         s = s.replace(i[0],self.RandomIP())
            #         print('randomIP')
            #     else:
            #         s = s.replace(i[0],i[1])
            #         print(s)
        s = s.replace('{randomnum}',str(random.randint(1,100))+str(random.randint(1,10))+str(random.randint(1,100)))
        s = s.replace('{randomip}',self.RandomIP())
        s = s.replace('{randomstr}',''.join(random.sample('zxcvbnmasdfghjklqwertyuiop',6)))
        s = s.replace('{randomnum3}',str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9)))
        # s = s.replace('{vehicles_id}',str(self.Vehiclesiddict['vehicles_id'][-1]))
        print(s)
        print("end\n")

        return s

    def RandomIP(self):
        IP = '10.22.{}.{}'.format(random.randint(1,255),random.randint(1,255))
        return IP



def main():
    app = QApplication(sys.argv)
    gui = Show()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()