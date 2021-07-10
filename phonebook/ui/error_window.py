from ui.error import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QMessageBox


def show_error_message(error_message: str):
    msg = QMessageBox()
    msg.setWindowTitle("You've input invalid data ")
    msg.setText(error_message)
    msg.exec_()