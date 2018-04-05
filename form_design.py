# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 419)
        Form.setMinimumSize(QtCore.QSize(640, 419))
        Form.setMaximumSize(QtCore.QSize(640, 419))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/lock-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.save_button = QtWidgets.QPushButton(Form)
        self.save_button.setEnabled(False)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_2.addWidget(self.save_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setMaximumSize(QtCore.QSize(170, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.delete_file_button = QtWidgets.QPushButton(Form)
        self.delete_file_button.setMaximumSize(QtCore.QSize(170, 16777215))
        self.delete_file_button.setObjectName("delete_file_button")
        self.verticalLayout.addWidget(self.delete_file_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.file_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.file_name_lineEdit.setMaximumSize(QtCore.QSize(170, 16777215))
        self.file_name_lineEdit.setObjectName("file_name_lineEdit")
        self.verticalLayout.addWidget(self.file_name_lineEdit)
        self.add_file_button = QtWidgets.QPushButton(Form)
        self.add_file_button.setMaximumSize(QtCore.QSize(170, 16777215))
        self.add_file_button.setObjectName("add_file_button")
        self.verticalLayout.addWidget(self.add_file_button)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Passwords Manager"))
        self.save_button.setText(_translate("Form", "Save"))
        self.delete_file_button.setText(_translate("Form", "Delete File"))
        self.label.setText(_translate("Form", "New File Name"))
        self.add_file_button.setText(_translate("Form", "Add File"))

