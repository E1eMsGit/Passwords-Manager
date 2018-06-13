# -*- coding: utf-8 -*-
"""
=======================================================
Программа для хранения паролей.
=======================================================
Модуль функционала формы авторизации.
=======================================================
* При первом запуске создает файл с паролем авторизации (12345 по умолчанию).
* Сравнивает введеный пароль с паролем в файле password.bin.
* Открывает главную форму при совпадении паролей.
=======================================================
NOTES: Пароль авторизации можно изменить открыв password.bin
    в любом текстовом редакторе .
    Сборку файлов form_design.py и icons.py выполнял командами:
    pyuic5 .\security_form.ui -o .\security_form_design.py
    pyrcc5 .\icons.qrc -o  .\icons.py
    Для конвертации формы нужен файл .ui (создается в qt designer)
    Для конвертации иконок нужен файл .qrc (создается в текстовом редакторе)
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget

import login_form_design
from icons import *


class LoginDialog(QDialog):
    """
    Главное окно.
    """

    def __init__(self, bundle_dir, main_form):
        QDialog.__init__(self)

        self.bundle_dir = bundle_dir
        self.main_form = main_form

        self.ui = login_form_design.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/images/lock-icon.png"))

        self.file_name = "password.bin"
        self.password = ""

        self.search_password_file()

        self.ui.check_pushButton.clicked.connect(self.check_password)

    def search_password_file(self):
        """
        Ищет или создает файл с паролем для входа в программу.
        Изменить пароль можно в корневом каталоге приложения в файле password.bin
        любым текстовым редактором.
        :return:
        """
        default_password = "12345"

        try:
            with open(self.file_name, "r") as f:
                self.password = f.readline()
        except FileNotFoundError:
            with open(self.file_name, "w") as f:
                f.write(default_password)
            self.password = default_password

    def closeEvent(self, e):
        """
        Обработка закрытия окна.
        :param e:
        :return:
        """
        result = QMessageBox.question(
            self,
            self.windowTitle(),
            "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if result == QMessageBox.Yes:
            e.accept()
            QWidget.closeEvent(self, e)
        else:
            e.ignore()

    @QtCore.pyqtSlot()
    def check_password(self):
        """
        Проверяет совпадает ли пароль введеный пользователем с паролем
        находящемся в файле password.bin
        :return:
        """
        user_input = self.ui.password_lineEdit.text()

        if user_input == self.password:
            self.hide()
            self.main_form.show()
        else:
            QMessageBox.critical(
                self,
                self.windowTitle(),
                "Incorrect password!",
                QMessageBox.Ok,
                QMessageBox.Ok
            )
            self.ui.password_lineEdit.clear()
            self.ui.password_lineEdit.setFocus()


if __name__ == "__main__":
    print(__doc__)
