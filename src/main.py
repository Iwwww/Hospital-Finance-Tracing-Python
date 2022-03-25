import os
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QPushButton
from main_window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


def main():
    app = QApplication(sys.argv)
    MainWindow = MainWindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    os.environ.setdefault('DEBUG', 'True')
    main()
