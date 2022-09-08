import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import password_manager_window
from password_manager_window import *
import add_pass_widget


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.password_file = None
        self.password_dict = {}
        self.ui = Ui_password_manager_window()
        self.ui.setupUi(self)

        self.ui.create_pass_file.clicked.connect(self.create_password_file)
        self.ui.add_pass.clicked.connect(self.on_clicked_add_pass)
        self.ui.load_pass_file.clicked.connect(self.open_password_file)
        self.ui.watch_passs.clicked.connect(self.watch_dict)

    def open_password_file(self):
        password_file = QFileDialog.getOpenFileName(self, 'D:\git\Password_Manager', '')

        if password_file[0]:
            f = open(password_file[0], 'r')

            for line in f:
                site, log_pass = line.split(':')
                self.password_dict[site] = log_pass.split(',')
                # self.ui.plainTextEdit.appendPlainText(line)
            #    print(line)

    def watch_dict(self):
        for line, log_pass in self.password_dict.items():
            text = f'SITE - {line}  LOGIN - {log_pass[0]}, PASSWORD - {log_pass[1]}!!!!!! ПОШЛА ЖАРА!!!!!!!!!! '
            self.ui.plainTextEdit.appendPlainText(text)

    def on_clicked_add_pass(self):
        self.ui.add_pass = Add_Pass_Widget()
        self.ui.add_pass.show()

        # with open(path, 'r') as f:
        #   for line in f:
        #      site, log_pass = line.split(':')
        #      self.password_dict[site] = log_pass.split(",")
        #      print()

    def create_password_file(self):
        self.password_file = QFileDialog.getSaveFileName(self, 'D:\git\Password_Manager', '')

        # if initial_values is not None:
        #   for key, value in initial_values.items():
        #      self.add_password(key, value)


class Add_Pass_Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.password_file = 'passtest.pass'
        self.password_file = MyWin().password_file
        self.apw = add_pass_widget.Ui_add_password_window()
        self.apw.setupUi(self)

        self.apw.add_data.clicked.connect(self.add_password)

    def add_password(self):

        if not self.apw.add_site_line.text():
            msg = QtWidgets.QMessageBox.information(
                self,
                'Внимание',
                'Вы ничего не ввели, записывать нечего.'
            )
            return

        with open(self.apw.password_file, 'a+', encoding='UTF-8') as file:
            text = self.apw.add_site_line.text()
            file.write(f'Ваш текст - {text}')

            msg = QtWidgets.QMessageBox.information(
                self,
                'Успех',
                f'Введенные данные записаны в файл {self.password_file}.'
            )


'''
    def add_password(self, site, login, password):
        #self.mw.password_dict[site] = login, password

        if not self.upw.add_site_line.text():
            msg = QtWidgets.QMessageBox.information(
                self,
                'Внимание',
                'Вы ничего не ввели, записывать нечего.'
            )
            return

        file_name = self.mw.password_file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f'Ваш текст - {self.add_site_line.text()}')

        msg = QtWidgets.QMessageBox.information(
            self,
            'Успех',
            f'Введенные данные записаны в файл {file_name}.'
        )
       
        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                site = self.upw.add_site_line.text()
                login = self.upw.add_login_line.text()
                password = self.upw.add_pass_line.text()
                f.write(site + ':' + login + ', ' + password + '\n')
                msg = QtWidgets.QMessageBox.information(
                    self,
                    'Успех',
                    f'Введенные данные записаны в файл {self.password_file} .'
                )
'''

'''
    def add_password(self, site, login, password):
        self.mw.password_dict[site] = login, password
        site = self.upw.add_site_line.text()
        login = self.upw.add_login_line.text()
        password = self.upw.add_pass_line.text()

        if self.mw.password_file is not None:
            password_file = self.mw.password_file
            with open(self.mw.password_file, 'w') as f:
                f.write(site + ':' + login + ', ' + password + '\n')
                msg = QtWidgets.QMessageBox.information(
                    self,
                    'Успех',
                    f'Введенные данные записаны в файл .'
                )
'''

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec())
