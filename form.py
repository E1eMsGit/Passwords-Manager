import os
import pickle

from PyQt5 import QtCore, QtWidgets, uic


class MainWindow(QtWidgets.QWidget):
    """
    Главное окно.
    """

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        uic.loadUi("main_form.ui", self)
        self.file_name = None

        self.search_dir()
        self.update_files_list()

        self.add_file_button.clicked.connect(self.add_file)
        self.delete_file_button.clicked.connect(self.delete_file)
        self.listWidget.itemClicked.connect(self.on_item_clicked)
        self.save_button.clicked.connect(self.save_to_file)

    def search_dir(self):
        """
        Переходит в каталог Passwords.
        Если каталог еще не создан - создает.
        :return:
        """
        try:
            os.chdir("./Passwords")
        except FileNotFoundError:
            os.mkdir("./Passwords")
            os.chdir("./Passwords")

    def update_files_list(self):
        """
        Выводит список файлов находящихся в каталоге Passwords.
        :return:
        """
        for file in os.listdir("."):
            self.listWidget.addItem(file)

    def closeEvent(self, e):
        """
        Обработка закрытия окна.
        :param e:
        :return:
        """
        result = QtWidgets.QMessageBox.question(
            self,
            self.windowTitle(),
            "Are you sure you want to exit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
        else:
            e.ignore()

    @QtCore.pyqtSlot()
    def add_file(self):
        """
        Создает файл и обновляет список файлов.
        :return:
        """
        self.file_name = self.file_name_lineEdit.text()
        try:
            with open(self.file_name, "wb") as file:
                pickle.dump("name\t\tlogin\t\tpassword\n" + ("-" * 87), file)
        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(
                self,
                self.windowTitle(),
                "Input file name!",
                QtWidgets.QMessageBox.Ok,
                QtWidgets.QMessageBox.Ok
            )
        self.file_name_lineEdit.clear()
        self.listWidget.clear()
        self.update_files_list()

    @QtCore.pyqtSlot()
    def delete_file(self):
        """
        Удаляет выбранный файл и обновляет список файлов.
        :return:
        """
        deleting = QtWidgets.QMessageBox.question(
            self,
            self.windowTitle(),
            "Are you sure you want to delete this file from your computer?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        if deleting == QtWidgets.QMessageBox.Yes:
            try:
                os.remove(self.file_name)
            except (TypeError, FileNotFoundError):
                QtWidgets.QMessageBox.critical(
                    self,
                    self.windowTitle(),
                    "Select the file!",
                    QtWidgets.QMessageBox.Ok,
                    QtWidgets.QMessageBox.Ok
                )
            self.plainTextEdit.clear()
            self.plainTextEdit.setEnabled(False)
            self.save_button.setEnabled(False)
            self.listWidget.clear()
            self.update_files_list()
        else:
            pass

    @QtCore.pyqtSlot()
    def on_item_clicked(self):
        """
        Открывает выбранный файл и выводит его содержимое.
        :return:
        """
        self.plainTextEdit.setEnabled(True)
        self.save_button.setEnabled(True)
        self.file_name = self.sender().currentItem().text()

        with open(self.file_name, "rb") as file:
            self.plainTextEdit.setPlainText(pickle.load(file))

    @QtCore.pyqtSlot()
    def save_to_file(self):
        """
        Сохраняет содержимое QPlaneTextEdit в файл.
        :return:
        """
        with open(self.file_name, "wb") as file:
            pickle.dump(self.plainTextEdit.toPlainText(), file)


if __name__ == "__main__":
    print("Это модуль формы")
