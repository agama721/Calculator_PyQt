# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kaloiandjambazov/Documents/Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 80, 251, 21))
        self.plainTextEdit.setStyleSheet("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 130, 251, 151))
        self.gridLayoutWidget.setMaximumSize(QtCore.QSize(401, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_18.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 2, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setMaximumSize(QtCore.QSize(64, 32))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 1, 4, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 0, 3, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setMaximumSize(QtCore.QSize(67, 32))
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 0, 5, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 0, 4, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_26.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout.addWidget(self.pushButton_26, 3, 4, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 0, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_19.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 3, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 0, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setMaximumSize(QtCore.QSize(64, 32))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 0, 2, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_22.setMaximumSize(QtCore.QSize(67, 32))
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 1, 5, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_20.setMaximumSize(QtCore.QSize(64, 32))
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 2, 2, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_23.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_23, 2, 3, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_21.setMaximumSize(QtCore.QSize(64, 32))
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_21, 3, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_24.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout.addWidget(self.pushButton_24, 3, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(67, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 5, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_25.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout.addWidget(self.pushButton_25, 2, 4, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_27.setMaximumSize(QtCore.QSize(67, 32))
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout.addWidget(self.pushButton_27, 2, 5, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 0, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setMaximumSize(QtCore.QSize(65, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 1, 3, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(70, 110, 251, 21))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setMaximumSize(QtCore.QSize(74, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_2.addWidget(self.pushButton_30, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "0"))
        self.pushButton_18.setText(_translate("MainWindow", "1"))
        self.pushButton_9.setText(_translate("MainWindow", "5"))
        self.pushButton_12.setText(_translate("MainWindow", "X"))
        self.pushButton_15.setText(_translate("MainWindow", "9"))
        self.pushButton_17.setText(_translate("MainWindow", "Sqrt"))
        self.pushButton_16.setText(_translate("MainWindow", "??"))
        self.pushButton_8.setText(_translate("MainWindow", "4"))
        self.pushButton_26.setText(_translate("MainWindow", "+"))
        self.pushButton_7.setText(_translate("MainWindow", "MR"))
        self.pushButton_5.setText(_translate("MainWindow", "M+"))
        self.pushButton_19.setText(_translate("MainWindow", "0"))
        self.pushButton_13.setText(_translate("MainWindow", "7"))
        self.pushButton_14.setText(_translate("MainWindow", "8"))
        self.pushButton_22.setText(_translate("MainWindow", "X2"))
        self.pushButton_20.setText(_translate("MainWindow", "2"))
        self.pushButton_23.setText(_translate("MainWindow", "3"))
        self.pushButton_21.setText(_translate("MainWindow", "."))
        self.pushButton_6.setText(_translate("MainWindow", "MS"))
        self.pushButton_24.setText(_translate("MainWindow", "??"))
        self.pushButton_4.setText(_translate("MainWindow", "="))
        self.pushButton_25.setText(_translate("MainWindow", "-"))
        self.pushButton_27.setText(_translate("MainWindow", "1/x"))
        self.pushButton_11.setText(_translate("MainWindow", "MC"))
        self.pushButton_10.setText(_translate("MainWindow", "6"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))
        self.pushButton_30.setText(_translate("MainWindow", "Bacspace"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
