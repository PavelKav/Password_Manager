import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from main_gui_py import *
from working import *


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.password_file = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_4.clicked.connect(self.create_password_file)

    def create_password_file(self, path):
        self.ui.plainTextEdit.appendPlainText('файл создан')
        f = open('path.pass', 'a')
        self.password_file = path

        # if initial_values is not None:
        #   for key, value in initial_values.items():
        #      self.add_password(key, value)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec())
