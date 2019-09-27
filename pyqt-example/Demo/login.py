# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        self.tabWidget = QtWidgets.QTabWidget(Window)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 561, 261))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_login = QtWidgets.QWidget()
        self.tab_login.setObjectName("tab_login")
        self.quit_button = QtWidgets.QPushButton(self.tab_login)
        self.quit_button.setGeometry(QtCore.QRect(120, 160, 75, 23))
        self.quit_button.setObjectName("quit_button")
        self.display_text = QtWidgets.QTextBrowser(self.tab_login)
        self.display_text.setGeometry(QtCore.QRect(220, 60, 256, 121))
        self.display_text.setObjectName("display_text")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_login)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 70, 181, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.username = QtWidgets.QLabel(self.formLayoutWidget)
        self.username.setObjectName("username")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.username)
        self.username_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.username_input.setObjectName("username_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.username_input)
        self.password_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password_input.setObjectName("password_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_input)
        self.password = QtWidgets.QLabel(self.formLayoutWidget)
        self.password.setObjectName("password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.password)
        self.login_button = QtWidgets.QPushButton(self.tab_login)
        self.login_button.setGeometry(QtCore.QRect(30, 160, 75, 23))
        self.login_button.setObjectName("login_button")
        self.tabWidget.addTab(self.tab_login, "")
        self.tab_list = QtWidgets.QWidget()
        self.tab_list.setObjectName("tab_list")
        self.table_view = QtWidgets.QTableView(self.tab_list)
        self.table_view.setGeometry(QtCore.QRect(20, 30, 521, 201))
        self.table_view.setObjectName("table_view")
        self.list_button = QtWidgets.QPushButton(self.tab_list)
        self.list_button.setGeometry(QtCore.QRect(220, 0, 75, 23))
        self.list_button.setObjectName("list_button")
        self.tabWidget.addTab(self.tab_list, "")

        self.retranslateUi(Window)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Form"))
        self.tabWidget.setToolTip(_translate("Window", "<html><head/><body><p>登录</p></body></html>"))
        self.quit_button.setText(_translate("Window", "退出"))
        self.username.setText(_translate("Window", "用户名"))
        self.password.setText(_translate("Window", "密码"))
        self.login_button.setText(_translate("Window", "登录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_login), _translate("Window", "登录"))
        self.list_button.setText(_translate("Window", "按钮"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_list), _translate("Window", "列表"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QWidget()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
