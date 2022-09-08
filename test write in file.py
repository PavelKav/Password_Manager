from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 77)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 111, 81))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 150, 21))
        self.pushButton.setObjectName("pushButton")
        #        self.pushButton.clicked.connect(self.clicked)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите текст:"))
        self.pushButton.setText(_translate("MainWindow", "Записать текст в файл."))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.clicked)

    def clicked(self):
        if not self.lineEdit.text():
            msg = QtWidgets.QMessageBox.information(
                self,
                'Внимание',
                'Вы ничего не ввели, записывать нечего.'
            )
            return

        file_name = "file.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f'Ваш текст - {self.lineEdit.text()}')

        msg = QtWidgets.QMessageBox.information(
            self,
            'Успех',
            f'Введенные данные записаны в файл {file_name}.'
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())