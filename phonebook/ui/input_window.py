from PyQt5.QtWidgets import QDialog
from phonebook.ui.dialog import Ui_input_window
from phonebook.ui.design import Ui_MainWindow
from phonebook.store import Store
from phonebook.entities.record import Record


class DialogWindow(QDialog, Ui_input_window):
    def __init__(self, data=None):
        QDialog.__init__(self)
        self.setupUi(self)
        if data:
            self.f_name_line.setText(data[0].split()[0])
            self.l_name_line.setText(data[0].split()[1])
            self.number_line.setText(data[1])
        self.buttonBox.accepted.connect(self.add_record)
        self.buttonBox.rejected.connect(self.cancel)

    def cancel(self):
        self.close()

    def add_record(self):
        # try:
        first_name = self.f_name_line.text()
        last_name = self.l_name_line.text()
        phone_number = self.number_line.text()
        birth_date = self.dateEdit.date()
        store = Store()
        store.add_record(
            Record(first_name, last_name, phone_number, birth_date))
        store.close()
        # except:
