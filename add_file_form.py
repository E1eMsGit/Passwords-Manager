# -*- coding: utf-8 -*-
"""
=======================================================
Программа для хранения паролей.
=======================================================
Модуль функционала формы создания файла.
=======================================================
* Ввод имени нового файла паролей.
=======================================================
NOTES: Пароль авторизации можно изменить открыв password.bin
    в любом текстовом редакторе .
    Сборку файлов form_design.py и icons.py выполнял командами:
    pyuic5 .\add_file_form.ui -o .\add_file_form_design.py
    pyrcc5 .\icons.qrc -o  .\icons.py
    Для конвертации формы нужен файл .ui (создается в qt designer)
    Для конвертации иконок нужен файл .qrc (создается в текстовом редакторе)
"""
import os
import pickle

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox

import add_file_form_design
from icons import *


class AddFileDialog(QDialog):
    """
    Главное окно.
    """

    def __init__(self, main_form):
        QDialog.__init__(self)

        self.main_form = main_form

        self.ui = add_file_form_design.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/images/lock-icon.png"))

        self.ui.accept_pushButton.clicked.connect(self.add_file)

    @QtCore.pyqtSlot()
    def add_file(self):
        """
        Создает файл и обновляет список файлов.
        :return:
        """
        file_name = self.ui.file_name_lineEdit.text().strip()

        if file_name in os.listdir(os.getcwd()):
            QMessageBox.critical(
                self,
                self.windowTitle(),
                "File already exists",
                QMessageBox.Ok,
                QMessageBox.Ok
            )
            self.ui.file_name_lineEdit.clear()
            self.ui.file_name_lineEdit.setFocus()
        elif file_name == "":
            QMessageBox.critical(
                self,
                self.windowTitle(),
                "Enter file name!",
                QMessageBox.Ok,
                QMessageBox.Ok
            )
            self.ui.file_name_lineEdit.clear()
            self.ui.file_name_lineEdit.setFocus()
        else:
            with open(file_name, "wb") as file:
                pickle.dump("", file)
            self.ui.file_name_lineEdit.clear()
            self.main_form.file_name = file_name
            self.main_form.update_files_list()
            self.hide()


if __name__ == "__main__":
    print(__doc__)
