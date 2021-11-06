import time

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "C:\Program Files (x86)\chromedriver.exe"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 374)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 171, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 80, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 120, 171, 20))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ryan\'s Covid Survey Filler"))
        self.pushButton.setText(_translate("MainWindow", "Fill out Covid Form!"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def clicked(self):
        USERNAME = self.lineEdit.text()
        PASSWORD = self.lineEdit_2.text()
        print(USERNAME + " | " + PASSWORD)
        complete_survey(USERNAME, PASSWORD)


def complete_survey(USERNAME, PASSWORD):
    print(USERNAME + " | " + PASSWORD)
    driver = webdriver.Chrome(PATH)
    driver.get("https://patientconnect.bu.edu/home.aspx")
    print(driver.title)

    search = driver.find_element_by_name("j_username")
    search.send_keys(USERNAME)
    search = driver.find_element_by_name("j_password")
    search.send_keys(PASSWORD)

    driver.find_element_by_name("_eventId_proceed").click()
    driver.get("https://patientconnect.bu.edu//Mvc/Patients/QuarantineSurvey")
    driver.get("https://patientconnect.bu.edu/CheckIn/Survey/ShowAll/21")

    driver.find_element_by_class_name("required").click()
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/header/div/div[2]/input").click()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

