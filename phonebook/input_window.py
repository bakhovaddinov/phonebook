from phonebook.dialog import Ui_input_window
from PyQt5.QtWidgets import QDialog
from phonebook.store import Store
from phonebook.entities.record import Record
from phonebook.design import Ui_MainWindow



class DialogWindow(QDialog, Ui_input_window):
    def __init__(self, Mainwindow):
        self.mainwindow = Mainwindow
        QDialog.__init__(self)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.add_record)
        self.buttonBox.rejected.connect(self.cancel)
    
    def cancel(self):
        self.close()

    def add_record(self):
        try:
            first_name = self.f_name_line.text()
            last_name = self.l_name_line.text()
            phone_number = self.number_line.text()
            birth_date = self.dateEdit.date()
            store = Store()
            store.add_record(Record(first_name, last_name, phone_number, birth_date))
            store.close()
        except:
            self.mainwindow.error.setText('')
            