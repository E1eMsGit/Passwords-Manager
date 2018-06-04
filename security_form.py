from PyQt5 import QtCore, QtWidgets

import security_form_design


class SecurityDialog(QtWidgets.QDialog):
    """
    Главное окно.
    """

    def __init__(self, bundle_dir, main_form):
        QtWidgets.QDialog.__init__(self)

        self.bundle_dir = bundle_dir
        self.main_form = main_form

        self.ui = security_form_design.Ui_Form()
        self.ui.setupUi(self)

        self.file_name = "password.bin"
        self.password = None

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
            with open(self.file_name, "r") as f:
                self.password = f.readline()

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
            self.ui.password_lineEdit.clear()
            QtWidgets.QMessageBox.critical(self,
                                           self.windowTitle(),
                                           "Incorrect password!",
                                           QtWidgets.QMessageBox.Ok,
                                           QtWidgets.QMessageBox.Ok
                                           )


if __name__ == "__main__":
    print("Это модуль диалога входа")
