# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(170, 110, 341, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(260, 100, 77, 121))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_17 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_3.addWidget(self.pushButton_17)
        self.pushButton_div = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_div.setObjectName("pushButton_div")
        self.verticalLayout_3.addWidget(self.pushButton_div)
        self.pushButton_mul = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.verticalLayout_3.addWidget(self.pushButton_mul)
        self.pushButton_sub = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.verticalLayout_3.addWidget(self.pushButton_sub)
        self.pushButton_add = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout_3.addWidget(self.pushButton_add)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 241, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_2.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_0 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_0.setObjectName("pushButton_0")
        self.horizontalLayout_4.addWidget(self.pushButton_0)
        self.pushButton_point = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_point.setObjectName("pushButton_point")
        self.horizontalLayout_4.addWidget(self.pushButton_point)
        self.pushButton_eq = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.horizontalLayout_4.addWidget(self.pushButton_eq)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_work = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_work.setObjectName("textEdit_work")
        self.verticalLayout.addWidget(self.textEdit_work)
        self.textEdit_ans = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_ans.setEnabled(True)
        self.textEdit_ans.setReadOnly(True)
        self.textEdit_ans.setObjectName("textEdit_ans")
        self.verticalLayout.addWidget(self.textEdit_ans)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.pushButton_17.setText(_translate("MainWindow", "<-"))
        self.pushButton_div.setText(_translate("MainWindow", "/"))
        self.pushButton_mul.setText(_translate("MainWindow", "*"))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_point.setText(_translate("MainWindow", "."))
        self.pushButton_eq.setText(_translate("MainWindow", "="))
