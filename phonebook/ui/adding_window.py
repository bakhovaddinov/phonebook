from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from ui.dialog import Ui_adding_window
from ui.design import Ui_MainWindow
from store import Store
from ui.error_window import show_error_message
from entities.record import Record


class InputWindow(QDialog, Ui_adding_window):
    def __init__(self, store: Store, phone_number: str = None):
        QDialog.__init__(self)
        self.setupUi(self)
        if not store:
            raise ValueError("store cannot be empty")
        self.store = store
        if phone_number:
            self.previous_phone_number = phone_number
            record = self.store.get_record(self.previous_phone_number)
            self.f_name_line.setText(record.first_name)
            self.l_name_line.setText(record.last_name)
            self.number_line.setText(record.phone_number)
            if record.birth_date:
                self.dateEdit.setDate(QtCore.QDate.fromString(record.birth_date))

            self.buttonBox.accepted.connect(self.edit_record)
        else:
            self.buttonBox.accepted.connect(self.add_record)
        self.buttonBox.rejected.connect(self.cancel)
    def accept(self):
        # super().accept()
        pass

    def cancel(self):
        self.close()

    def edit_record(self):
        try:
            self.store.update_record(self.previous_phone_number, self._make_record())
            super().accept()
        except ValueError as error:
            show_error_message(str(error))

    def _make_record(self) -> Record:
        record = Record(self.f_name_line.text(), self.l_name_line.text(), self.number_line.text(), self.dateEdit.date())
        return record

    def add_record(self):
        try:
            self.store.add_record(self._make_record())
            super().accept()
        except ValueError as error:
            show_error_message(str(error))
