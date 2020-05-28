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
        Form.resize(433, 377)
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(50, 50, 161, 20))
        self.name.setObjectName("name")
        self.meanings = QtWidgets.QTextBrowser(Form)
        self.meanings.setGeometry(QtCore.QRect(10, 100, 201, 121))
        self.meanings.setObjectName("meanings")
        self.origins = QtWidgets.QTextBrowser(Form)
        self.origins.setGeometry(QtCore.QRect(10, 250, 201, 121))
        self.origins.setObjectName("origins")
        self.new_meaning = QtWidgets.QTextEdit(Form)
        self.new_meaning.setGeometry(QtCore.QRect(220, 70, 201, 121))
        self.new_meaning.setObjectName("new_meaning")
        self.new_origin = QtWidgets.QTextEdit(Form)
        self.new_origin.setGeometry(QtCore.QRect(220, 220, 201, 121))
        self.new_origin.setObjectName("new_origin")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 50, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(230, 50, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(240, 200, 71, 16))
        self.label_5.setObjectName("label_5")
        self.ok = QtWidgets.QPushButton(Form)
        self.ok.setGeometry(QtCore.QRect(340, 350, 75, 23))
        self.ok.setObjectName("ok")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")

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
        self.label_6.setText(_translate("Form", "注：å, e̊, o̊, ī, z̄, ü 分别用ar, er, or, ir, zr, v 表示"))
