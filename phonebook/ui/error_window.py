from phonebook.ui.error import Ui_Dialog
from PyQt5.QtWidgets import QDialog


class ErrorWindow(Ui_Dialog, QDialog):
    def __init__(self, error_msg):
        QDialog.__init__(self)
        self.setupUi(self)
        self.error_btn.clicked.connect(self.close_func)
        self.error_label.setText(error_msg)
    
    def close_func(self):
        self.close()