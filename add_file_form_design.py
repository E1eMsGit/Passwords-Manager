# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_file_form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(225, 165)
        Form.setMinimumSize(QtCore.QSize(225, 165))
        Form.setMaximumSize(QtCore.QSize(225, 165))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(198, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 3)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.file_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.file_name_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.file_name_lineEdit.setObjectName("file_name_lineEdit")
        self.gridLayout.addWidget(self.file_name_lineEdit, 3, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(123, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(57, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        self.accept_pushButton = QtWidgets.QPushButton(Form)
        self.accept_pushButton.setObjectName("accept_pushButton")
        self.gridLayout.addWidget(self.accept_pushButton, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(57, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(123, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 6, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add password file"))
        self.label.setText(_translate("Form", "Enter file name"))
        self.accept_pushButton.setText(_translate("Form", "Accept"))

