# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(433, 340)
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(50, 10, 161, 20))
        self.name.setObjectName("name")
        self.meanings = QtWidgets.QTextBrowser(Form)
        self.meanings.setGeometry(QtCore.QRect(10, 60, 201, 121))
        self.meanings.setObjectName("meanings")
        self.origins = QtWidgets.QTextBrowser(Form)
        self.origins.setGeometry(QtCore.QRect(10, 210, 201, 121))
        self.origins.setObjectName("origins")
        self.new_meaning = QtWidgets.QTextEdit(Form)
        self.new_meaning.setGeometry(QtCore.QRect(220, 30, 201, 121))
        self.new_meaning.setObjectName("new_meaning")
        self.new_origin = QtWidgets.QTextEdit(Form)
        self.new_origin.setGeometry(QtCore.QRect(220, 180, 201, 121))
        self.new_origin.setObjectName("new_origin")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(230, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(240, 160, 71, 16))
        self.label_5.setObjectName("label_5")
        self.ok = QtWidgets.QPushButton(Form)
        self.ok.setGeometry(QtCore.QRect(340, 310, 75, 23))
        self.ok.setObjectName("ok")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "词汇："))
        self.label_2.setText(_translate("Form", "释义："))
        self.label_3.setText(_translate("Form", "词源："))
        self.label_4.setText(_translate("Form", "输入新释义："))
        self.label_5.setText(_translate("Form", "输入新词源："))
        self.ok.setText(_translate("Form", "确定"))
