# -*- coding: utf-8 -*-
"""
=======================================================
Программа для хранения паролей.
=======================================================
Главный модуль.
=======================================================
* Проверяет запускается ли программа как скомпилированный файл или как скрипт;
* Запускает программу;
=======================================================
NOTES: Сборку в один файл делал через PyInstaller.
Пример команды:
    pyinstaller --onefile --icon=name.ico --noconsole myscript.py
"""
import os
import sys

from PyQt5.QtWidgets import QApplication

from form import MainWindow


def main():
    if getattr(sys, "frozen", False):
        bundle_dir = os.path.dirname(sys.executable)
    else:
        bundle_dir = os.path.dirname(os.path.abspath(__file__))

    app = QApplication(sys.argv)

    MainWindow(bundle_dir)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
