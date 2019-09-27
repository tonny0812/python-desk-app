# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(489, 228)
        Form.setMinimumSize(QtCore.QSize(489, 228))
        Form.setMaximumSize(QtCore.QSize(489, 228))
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(20, 60, 41, 16))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(20, 100, 41, 16))
        self.password.setObjectName("password")
        self.login_button = QtWidgets.QPushButton(Form)
        self.login_button.setGeometry(QtCore.QRect(30, 150, 75, 23))
        self.login_button.setObjectName("login_button")
        self.quit_button = QtWidgets.QPushButton(Form)
        self.quit_button.setGeometry(QtCore.QRect(120, 150, 75, 23))
        self.quit_button.setObjectName("quit_button")
        self.username_input = QtWidgets.QLineEdit(Form)
        self.username_input.setGeometry(QtCore.QRect(70, 60, 113, 20))
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(Form)
        self.password_input.setGeometry(QtCore.QRect(70, 100, 113, 20))
        self.password_input.setObjectName("password_input")
        self.display_text = QtWidgets.QTextBrowser(Form)
        self.display_text.setGeometry(QtCore.QRect(220, 50, 256, 121))
        self.display_text.setObjectName("display_text")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.username.setText(_translate("Form", "用户名"))
        self.password.setText(_translate("Form", "密码"))
        self.login_button.setText(_translate("Form", "登录"))
        self.quit_button.setText(_translate("Form", "退出"))
