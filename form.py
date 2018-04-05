import os
import pickle

from PyQt5 import QtCore, QtWidgets, uic
import form_design

class MainWindow(QtWidgets.QWidget):
    """
    Главное окно.
    """

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.ui = form_design.Ui_Form()
        self.ui.setupUi(self)

        self.bundle_dir = os.path.dirname(os.path.abspath(__file__))

        self.file_name = None

        self.search_dir()
        self.update_files_list()

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
        for file in os.listdir("."):
            self.ui.listWidget.addItem(file)

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
        self.file_name = self.ui.file_name_lineEdit.text()
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
        self.ui.file_name_lineEdit.clear()
        self.ui.listWidget.clear()
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
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.setEnabled(False)
            self.ui.save_button.setEnabled(False)
            self.ui.listWidget.clear()
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


if __name__ == "__main__":
    print("Это модуль формы")
