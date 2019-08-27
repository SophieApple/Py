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
        self.vehicles_Massage['vehicles_id'] = []
        self.vehicles_Massage['order_template_id'] = []
        self.vehicles_Massage['order_id'] = []
        self.vehicles_Massage['map_id'] = []
        self.vehicles_Massage['map_relation_id'] = []
        self.vehicles_Massage['station_id'] = []
        self.vehicles_Massage['action_template_id'] = []
        self.vehicles_Massage['dashboard_template_id'] = []
        self.vehicles_Massage['caller_id'] = []
        self.vehicles_Massage['charger_id'] = []
        while True:
            a = []
            try:
                re = requests.get(url='http://192.168.83.200:8088/api/vehicles',headers={"token":"ZGV2LDE1Njg4NjQ0NDY4MDIsZjM3NmFmMTkzZTUwOTczMWU5OTY5ZjFlNjFjZTlmZTM=","cookie":'username=2|1:0|10:1565933869|8:username|4:ZGV2|1a8418e48b008340cf53d338f3085098f1349003a4a984c03b65e7280d47fc9e; userid="2|1:0|10:1565933869|6:userid|4:Mg==|c96070cf9ea41a922930b4d9340be76ab2e053634326689d4de847679d906ddc"'})
                for i in json.loads(re.text)['vehicles']:
                    a.append(i['id'])
                self.vehicles_Massage['vehicles_id'] = a
                a = []
            except Exception as e:
                print(e)

            try:
                template_re = requests.get(url='http://192.168.83.200:8088/api/templates/order',headers={"token":"ZGV2LDE1Njg4NjQ0NDY4MDIsZjM3NmFmMTkzZTUwOTczMWU5OTY5ZjFlNjFjZTlmZTM=","cookie":'username=2|1:0|10:1565933869|8:username|4:ZGV2|1a8418e48b008340cf53d338f3085098f1349003a4a984c03b65e7280d47fc9e; userid="2|1:0|10:1565933869|6:userid|4:Mg==|c96070cf9ea41a922930b4d9340be76ab2e053634326689d4de847679d906ddc"'})
                for i in json.loads(template_re.text)['templates']:
                    a.append(i['id'])
                self.vehicles_Massage['order_template_id'] = a
                a = []
            except Exception as e:
                print(e)

            try:
                order_id_re = requests.get(url='http://192.168.83.200:8088/api/orders',headers={"token":"ZGV2LDE1Njg4NjQ0NDY4MDIsZjM3NmFmMTkzZTUwOTczMWU5OTY5ZjFlNjFjZTlmZTM=","cookie":'username=2|1:0|10:1565933869|8:username|4:ZGV2|1a8418e48b008340cf53d338f3085098f1349003a4a984c03b65e7280d47fc9e; userid="2|1:0|10:1565933869|6:userid|4:Mg==|c96070cf9ea41a922930b4d9340be76ab2e053634326689d4de847679d906ddc"'})
                for i in json.loads(order_id_re.text)['orders']:
                    a.append(i['id'])
                self.vehicles_Massage['order_id'] = a
                a = []
            except Exception as e:
                print(e)

            try:
                map_id_re = requests.get(url='http://192.168.83.200:8088/api/maps',headers={"token":"ZGV2LDE1Njg4NjQ0NDY4MDIsZjM3NmFmMTkzZTUwOTczMWU5OTY5ZjFlNjFjZTlmZTM=","cookie":'username=2|1:0|10:1565933869|8:username|4:ZGV2|1a8418e48b008340cf53d338f3085098f1349003a4a984c03b65e7280d47fc9e; userid="2|1:0|10:1565933869|6:userid|4:Mg==|c96070cf9ea41a922930b4d9340be76ab2e053634326689d4de847679d906ddc"'})
                for i in json.loads(map_id_re.text)['maps']:
                    a.append(i['id'])
                self.vehicles_Massage['map_id'] = a
                a = []
            except Exception as e:
                print(e)

            try:
                map_relation_id_re = requests.get(url='http://192.168.83.200:8088/api/maps/relations',headers={"token":"ZGV2LDE1Njg4NjQ0NDY4MDIsZjM3NmFmMTkzZTUwOTczMWU5OTY5ZjFlNjFjZTlmZTM=","cookie":'username=2|1:0|10:1565933869|8:username|4:ZGV2|1a8418e48b008340cf53d338f3085098f1349003a4a984c03b65e7280d47fc9e; userid="2|1:0|10:1565933869|6:userid|4:Mg==|c96070cf9ea41a922930b4d9340be76ab2e053634326689d4de847679d906ddc"'})
                for i in json.loads(map_relation_id_re.text)['relations']:
                    a.append(i['id'])
                self.vehicles_Massage['map_relation_id'] = a
                a = []
            except Exception as e:
                print(e)

            try:
                station_id_re = requests.get(url='http://192.168.83.200:8088/api/maps/station',headers={"token":"ZGV2LDE1Njg4NjQ0NDY4MDIsZjM3NmFmMTkzZTUwOTczMWU5OTY5ZjFlNjFjZTlmZTM=","cookie":'username=2|1:0|10:1565933869|8:username|4:ZGV2|1a8418e48b008340cf53d338f3085098f1349003a4a984c03b65e7280d47fc9e; userid="2|1:0|10:1565933869|6:userid|4:Mg==|c96070cf9ea41a922930b4d9340be76ab2e053634326689d4de847679d906ddc"'})
                for i in json.loads(station_id_re.text)['stations']:
                    a.append(i['id'])
                self.vehicles_Massage['station_id'] = a
                a = []
            except Exception as e:
                print(e)

            try:
                action_template_id_re = requests.get(url='http://192.168.83.200:8088/api/templates/action',headers={"token":"ZGV2LDE1Njg4NjQ0NDY4MDIsZjM3NmFmMTkzZTUwOTczMWU5OTY5ZjFlNjFjZTlmZTM=","cookie":'username=2|1:0|10:1565933869|8:username|4:ZGV2|1a8418e48b008340cf53d338f3085098f1349003a4a984c03b65e7280d47fc9e; userid="2|1:0|10:1565933869|6:userid|4:Mg==|c96070cf9ea41a922930b4d9340be76ab2e053634326689d4de847679d906ddc"'})
                for i in json.loads(action_template_id_re.text)['templates']:
                    a.append(i['id'])
                self.vehicles_Massage['action_template_id'] = a
                a = []
            except Exception as e:
                print(e)

            try:
                dashboard_template_id_re = requests.get(url='http://192.168.83.200:8088/api/templates/dashboard', headers={
                    "token": "ZGV2LDE1Njg4NjQ0NDY4MDIsZjM3NmFmMTkzZTUwOTczMWU5OTY5ZjFlNjFjZTlmZTM=",
                    "cookie": 'username=2|1:0|10:1565933869|8:username|4:ZGV2|1a8418e48b008340cf53d338f3085098f1349003a4a984c03b65e7280d47fc9e; userid="2|1:0|10:1565933869|6:userid|4:Mg==|c96070cf9ea41a922930b4d9340be76ab2e053634326689d4de847679d906ddc"'})
                for i in json.loads(dashboard_template_id_re.text)['templates']:
                    a.append(i['id'])
                self.vehicles_Massage['dashboard_template_id'] = a
                a = []
            except Exception as e:
                print(e)

            try:
                caller_id_re = requests.get(url='http://192.168.83.200:8088/api/devices/caller', headers={
                    "token": "ZGV2LDE1Njg4NjQ0NDY4MDIsZjM3NmFmMTkzZTUwOTczMWU5OTY5ZjFlNjFjZTlmZTM=",
                    "cookie": 'username=2|1:0|10:1565933869|8:username|4:ZGV2|1a8418e48b008340cf53d338f3085098f1349003a4a984c03b65e7280d47fc9e; userid="2|1:0|10:1565933869|6:userid|4:Mg==|c96070cf9ea41a922930b4d9340be76ab2e053634326689d4de847679d906ddc"'})
                for i in json.loads(caller_id_re.text)['callers']:
                    a.append(i['id'])
                self.vehicles_Massage['caller_id'] = a
                a = []
            except Exception as e:
                print(e)

            try:
                charger_id_re = requests.get(url='http://192.168.83.200:8088/api/devices/charger', headers={
                    "token": "ZGV2LDE1Njg4NjQ0NDY4MDIsZjM3NmFmMTkzZTUwOTczMWU5OTY5ZjFlNjFjZTlmZTM=",
                    "cookie": 'username=2|1:0|10:1565933869|8:username|4:ZGV2|1a8418e48b008340cf53d338f3085098f1349003a4a984c03b65e7280d47fc9e; userid="2|1:0|10:1565933869|6:userid|4:Mg==|c96070cf9ea41a922930b4d9340be76ab2e053634326689d4de847679d906ddc"'})
                for i in json.loads(charger_id_re.text)['chargers']:
                    a.append(i['id'])
                self.vehicles_Massage['charger_id'] = a
                a = []
            except Exception as e:
                print(e)


            self.trigget.emit(self.vehicles_Massage)
            time.sleep(5)
            # print(self.vehicles_Massage)

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
            url = self.ReplaceStr("{}{}".format(host, self.list['path'][i]))
            print(url)
            Mark = True
            if not self.list['headers'].isnull()[i]:
                try:
                    header = json.loads(self.ReplaceStr(self.list['headers'][i]))
                    print(header)
                except Exception as e:
                    logging.exception(e)
                    Mark = False
            if not self.list['params'].isnull()[i]:
                try:
                    param = json.loads(self.ReplaceStr(self.list['params'][i]))
                    print(param)
                except Exception as e:
                    logging.exception(e)
                    Mark = False

            if not self.list['body'].isnull()[i]:
                try:
                    body = json.loads(self.ReplaceStr(self.list['body'][i]))
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

        # s = '{'+s.strip('{').strip('}').format(randomnum = str(random.randint(1,100))+str(random.randint(1,10))+str(random.randint(1,100)),
        #              randomip = self.RandomIP(),
        #              randomstr = ''.join(random.sample('zxcvbnmasdfghjklqwertyuiop',6)),
        #              randomnum3 = str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9)),
        #              randomnum2 = str(random.randint(1,9))+str(random.randint(1,9)),
        #              randomnum1 = str(random.randint(1,9)),
        #              )+'}'
        # print(s)

        s = s.replace('{randomnum}',str(random.randint(1,100))+str(random.randint(1,10))+str(random.randint(1,100)))
        s = s.replace('{randomip}',self.RandomIP())
        s = s.replace('{randomstr}',''.join(random.sample('zxcvbnmasdfghjklqwertyuiop',6)))
        s = s.replace('{randomnum3}',str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9)))
        s = s.replace('{randomnum2}',str(random.randint(1,9))+str(random.randint(1,9)))
        s = s.replace('{randomnum1}',str(random.randint(1,9)))


        try:
            s = s.replace('{vehicles_id}',str(random.choice(self.Vehiclesiddict['vehicles_id'])))
        except Exception as e:
            print('vehicles_id',e)

        try:
            s = s.replace('{order_template_id}',str(random.choice(self.Vehiclesiddict['order_template_id'])))
        except Exception as e:
            print('order_template_id',e)

        try:
            s = s.replace('{order_id}',str(random.choice(self.Vehiclesiddict['order_id'])))
        except Exception as e:
            print('order_id',e)

        try:
            s = s.replace('{map_id}',str(random.choice(self.Vehiclesiddict['map_id'])))
        except Exception as e:
            print('map_id',e)

        try:
            s = s.replace('{map_relation_id}',str(random.choice(self.Vehiclesiddict['map_relation_id'])))
        except Exception as e:
            print('map_relation_id',e)

        try:
            s = s.replace('{station_id}',str(random.choice(self.Vehiclesiddict['station_id'])))
        except Exception as e:
            print('station_id',e)

        try:
            s = s.replace('{action_template_id}',str(random.choice(self.Vehiclesiddict['action_template_id'])))
        except Exception as e:
            print('action_template_id',e)

        try:
            s = s.replace('{dashboard_template_id}',str(random.choice(self.Vehiclesiddict['dashboard_template_id'])))
        except Exception as e:
            print('dashboard_template_id',e)

        try:
            s = s.replace('{caller_id}',str(random.choice(self.Vehiclesiddict['caller_id'])))
        except Exception as e:
            print('caller_id',e)

        try:
            s = s.replace('{charger_id}',str(random.choice(self.Vehiclesiddict['charger_id'])))
        except Exception as e:
            print('charger_id',e)

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