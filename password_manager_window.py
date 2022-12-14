# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password_manager_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_password_manager_window(object):
    def setupUi(self, password_manager_window):
        password_manager_window.setObjectName("password_manager_window")
        password_manager_window.resize(1114, 600)
        password_manager_window.setMinimumSize(QtCore.QSize(1114, 600))
        password_manager_window.setMaximumSize(QtCore.QSize(1114, 600))
        self.centralwidget = QtWidgets.QWidget(password_manager_window)
        self.centralwidget.setObjectName("centralwidget")
        self.create_key_file = QtWidgets.QPushButton(self.centralwidget)
        self.create_key_file.setGeometry(QtCore.QRect(0, 0, 150, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.create_key_file.setFont(font)
        self.create_key_file.setObjectName("create_key_file")
        self.load_key_file = QtWidgets.QPushButton(self.centralwidget)
        self.load_key_file.setGeometry(QtCore.QRect(150, 0, 150, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.load_key_file.setFont(font)
        self.load_key_file.setObjectName("load_key_file")
        self.create_pass_file = QtWidgets.QPushButton(self.centralwidget)
        self.create_pass_file.setGeometry(QtCore.QRect(300, 0, 180, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.create_pass_file.setFont(font)
        self.create_pass_file.setObjectName("create_pass_file")
        self.load_pass_file = QtWidgets.QPushButton(self.centralwidget)
        self.load_pass_file.setGeometry(QtCore.QRect(480, 0, 180, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.load_pass_file.setFont(font)
        self.load_pass_file.setObjectName("load_pass_file")
        self.add_pass = QtWidgets.QPushButton(self.centralwidget)
        self.add_pass.setGeometry(QtCore.QRect(660, 0, 150, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_pass.setFont(font)
        self.add_pass.setObjectName("add_pass")
        self.watch_passs = QtWidgets.QPushButton(self.centralwidget)
        self.watch_passs.setGeometry(QtCore.QRect(810, 0, 150, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.watch_passs.setFont(font)
        self.watch_passs.setObjectName("watch_passs")
        self.watch_pass = QtWidgets.QPushButton(self.centralwidget)
        self.watch_pass.setGeometry(QtCore.QRect(960, 0, 150, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.watch_pass.setFont(font)
        self.watch_pass.setObjectName("watch_pass")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 50, 541, 531))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(560, 50, 541, 531))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        password_manager_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(password_manager_window)
        QtCore.QMetaObject.connectSlotsByName(password_manager_window)

    def retranslateUi(self, password_manager_window):
        _translate = QtCore.QCoreApplication.translate
        password_manager_window.setWindowTitle(_translate("password_manager_window", "MainWindow"))
        self.create_key_file.setText(_translate("password_manager_window", "?????????????? ???????? "))
        self.load_key_file.setText(_translate("password_manager_window", "?????????????????? ????????"))
        self.create_pass_file.setText(_translate("password_manager_window", "?????????????? ???????? ?? ????????????????"))
        self.load_pass_file.setText(_translate("password_manager_window", "?????????????????? ???????? ?? ????????????????"))
        self.add_pass.setText(_translate("password_manager_window", "???????????????? ????????????"))
        self.watch_passs.setText(_translate("password_manager_window", "???????????????????? ?????? ????????????"))
        self.watch_pass.setText(_translate("password_manager_window", "???????????????? ????????????"))
