# -*- coding: utf-8 -*-
"""
=======================================================
Программа для хранения паролей.
=======================================================
Модуль функционала основной формы.
=======================================================
* Вызывает диалоговое окно авторизации.
* При первом запуске создает каталог для хранения файлов с паролями.
* Заполняет list widget списком файлов из каталога с паролями.
* Добавление и удаление файлов с паролями.
* Сохранение содержимого plain text edit в выбранный файл.
=======================================================
NOTES: Сборку файлов form_design.py и icons.py выполнял командами:
    pyuic5 .\main_form.ui -o .\form_design.py
    pyrcc5 .\icons.qrc -o  .\icons.py
    Для конвертации формы нужен файл .ui (создается в qt designer)
    Для конвертации иконок нужен файл .qrc (создается в текстовом редакторе)
"""
import os
import pickle

from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QMessageBox, QWidget, QAction

import form_design
from add_file_form import AddFileDialog
from icons import *
from login_form import LoginDialog


class MainWindow(QWidget):
    """
    Главное окно.
    """

    def __init__(self, bundle_dir):
        QWidget.__init__(self)

        self.login_dialog = LoginDialog(bundle_dir, self)
        self.bundle_dir = bundle_dir

        self.ui = form_design.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/images/lock-icon.png"))
        self.ui.add_file_button.setIcon(QIcon(":/images/add.png"))
        self.ui.delete_file_button.setIcon(QIcon(":/images/delete.png"))
        self.ui.save_button.setIcon(QIcon(":/images/save.png"))

        self.file_name = ""

        self.login_dialog.show()
        self.search_dir()
        self.update_files_list()

        plain_text_save_shortcut = QAction(self.ui.plainTextEdit)
        plain_text_save_shortcut.setShortcut(QKeySequence("Ctrl+S"))
        self.ui.plainTextEdit.addAction(plain_text_save_shortcut)
        plain_text_save_shortcut.triggered.connect(self.save_to_file)

        list_widget_delete_shortcut = QAction(self.ui.listWidget)
        list_widget_delete_shortcut.setShortcut(QKeySequence("Delete"))
        self.ui.plainTextEdit.addAction(list_widget_delete_shortcut)
        list_widget_delete_shortcut.triggered.connect(self.delete_file)

        self.ui.add_file_button.clicked.connect(self.add_file)
        self.ui.delete_file_button.clicked.connect(self.delete_file)
        self.ui.listWidget.itemClicked.connect(self.on_item_clicked)
        self.ui.save_button.clicked.connect(self.save_to_file)

    def search_dir(self):
        """
        Переходит в каталог Passwords.
        Если каталог еще не создан - создает.
        :return:
        """
        try:
            os.chdir(os.path.join(self.bundle_dir, "Passwords"))
        except FileNotFoundError:
            os.mkdir(os.path.join(self.bundle_dir, "Passwords"))
            os.chdir(os.path.join(self.bundle_dir, "Passwords"))

    def update_files_list(self):
        """
        Выводит список файлов находящихся в каталоге Passwords.
        :return:
        """
        self.file_name = ""

        self.ui.listWidget.clear()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.setEnabled(False)
        self.ui.delete_file_button.setEnabled(False)
        self.ui.save_button.setEnabled(False)

        for file in os.listdir(os.getcwd()):
            self.ui.listWidget.addItem(file)

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
    def add_file(self):
        """
        Создает файл и обновляет список файлов.
        :return:
        """
        add_file_dialog = AddFileDialog(self)
        add_file_dialog.exec_()

    @QtCore.pyqtSlot()
    def delete_file(self):
        """
        Удаляет выбранный файл и обновляет список файлов.
        :return:
        """
        result = QMessageBox.question(
            self,
            self.windowTitle(),
            "Are you sure you want to delete this file from your computer?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if result == QMessageBox.Yes:
            os.remove(self.file_name)
            self.update_files_list()
        else:
            pass

    @QtCore.pyqtSlot()
    def on_item_clicked(self):
        """
        Открывает выбранный файл и выводит его содержимое.
        :return:
        """
        self.ui.plainTextEdit.setEnabled(True)
        self.ui.delete_file_button.setEnabled(True)
        self.ui.save_button.setEnabled(True)
        self.file_name = self.sender().currentItem().text()

        with open(self.file_name, "rb") as file:
            self.ui.plainTextEdit.setPlainText(pickle.load(file))

    @QtCore.pyqtSlot()
    def save_to_file(self):
        """
        Сохраняет содержимое QPlaneTextEdit в файл.
        :return:
        """
        with open(self.file_name, "wb") as file:
            pickle.dump(self.ui.plainTextEdit.toPlainText(), file)

        QMessageBox.information(
            self,
            self.windowTitle(),
            "Changes saved",
            QMessageBox.Ok,
            QMessageBox.Ok
        )


if __name__ == "__main__":
    print(__doc__)
