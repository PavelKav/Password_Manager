import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from password_manager_window import *
from working import *
from add_pass_widget import Ui_add_password_window


class Add_Pass_Widget(QtWidgets.QWidget, Ui_add_password_window):
    def __init__(self, parent=None):
        super(Add_Pass_Widget, self).__init__(parent)
        self.setupUi(self)


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.password_file = None
        self.password_dict = {}
        self.ui = Ui_password_manager_window()
        self.ui.setupUi(self)

        self.ui.create_pass_file.clicked.connect(self.create_password_file)
        self.ui.add_pass.clicked.connect(self.onClickedAddPass)
        self.ui.load_pass_file.clicked.connect(self.open_password_file)
        self.ui.watch_passs.clicked.connect(self.watch_dict)

    def open_password_file(self):
        path = QFileDialog.getOpenFileName(self, 'D:\git\Password_Manager', '')

        if path[0]:
            f = open(path[0], 'r')

            for line in f:
                site, log_pass = line.split(':')
                self.password_dict[site] = log_pass.split(',')
                #self.ui.plainTextEdit.appendPlainText(line)
            #    print(line)

    def watch_dict(self):
        for line, log_pass in self.password_dict.items():
            #site, log_pass = line.split(':')
            #login_password = log_pass.split(',')
            #print(f' login {site}')
            #print(log_pass)
            #print(login_password)
            text = f'SITE - {line}  LOGIN - {log_pass[0]}, PASSWORD - {log_pass[1]}!!!!!! ПОШЛА ЖАРА!!!!!!!!!! '
            self.ui.plainTextEdit.appendPlainText(text)

    def onClickedAddPass(self):
        self.add_pass = Add_Pass_Widget()
        self.add_pass.show()

        # with open(path, 'r') as f:
        #   for line in f:
        #      site, log_pass = line.split(':')
        #     self.password_dict[site] = log_pass.split(",")
        #    print()

    def create_password_file(self):
        path = QFileDialog.getSaveFileName(self, 'D:\git\Password_Manager', '')

        # if initial_values is not None:
        #   for key, value in initial_values.items():
        #      self.add_password(key, value)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec())
