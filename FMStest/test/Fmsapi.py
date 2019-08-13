from .UI import Ui_MianWIndow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui
import sys,requests

class Show(QMainWindow,Ui_MianWIndow):
    def __init__(self):
        super(Show, self).__init__()
