import sys

from PyQt5 import QtCore, QtWidgets

from guiocr import __appname__
from guiocr.app import MainWindow


def main():
    QtCore.QCoreApplication.setOrganizationDomain("casia")
    QtCore.QCoreApplication.setApplicationName(__appname__)
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName(__appname__)
    # app.setWindowIcon(newIcon("icon"))
    win = MainWindow()
    # win = createWindow(win,'blue')

    win.show()
    win.raise_()
    sys.exit(app.exec_())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
