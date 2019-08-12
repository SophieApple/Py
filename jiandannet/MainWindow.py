from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtGui import *
import sys

class UI_MainWindow(QMainWindow):
    def __init__(self):
        super(UI_MainWindow, self).__init__()
        self.setWindowTitle('jiandannet')
        self.resize(600,480)
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def Pixmap(self,data):
        photo = QPixmap()
        photo.loadFromData(data)
        self.main_layout.addWidget(photo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = UI_MainWindow()
    gui.show()
    sys.exit(app.exec_())