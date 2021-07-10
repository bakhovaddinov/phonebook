import sys
from PyQt5.QtWidgets import QApplication
from ui.mainwidget import MainWidget


def main():
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
