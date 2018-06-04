import os
import sys

from PyQt5 import QtWidgets

from form import MainWindow


def main():
    if getattr(sys, "frozen", False):
        bundle_dir = os.path.dirname(sys.executable)
    else:
        bundle_dir = os.path.dirname(os.path.abspath(__file__))

    app = QtWidgets.QApplication(sys.argv)

    MainWindow(bundle_dir)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
