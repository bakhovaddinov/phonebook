from PyQt5.QtWidgets import QMainWindow
from phonebook.store import Store
from phonebook.ui.design import Ui_MainWindow
from phonebook.ui.input_window import InputWindow
from phonebook.ui.error_window import ErrorWindow


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.store = Store()
        self.refresh()
        self.pushButton.clicked.connect(self.search_func)
        self.add_btn.clicked.connect(self.adding)
        self.rmv_btn.clicked.connect(self.remove)
        self.ed_btn.clicked.connect(self.edit)

    def adding(self):
        window = InputWindow()
        window.show()
        window.exec()
        self.refresh()

    def refresh(self):
        self.phonebook.clear()
        for element in self.store.show_records():
            self.phonebook.addItem(
                f'{element[0]} {element[1]}  —  {element[2]}  —  {element[3]}')

    def remove(self):
        data = self.phonebook.currentItem().text().split('  —  ')
        first_name, last_name = data[0].split()
        self.store.remove_record(first_name, last_name, data[1])
        self.refresh()

    def edit(self):
        data = self.phonebook.currentItem().text().split('  —  ')
        window = InputWindow(data=data)
        window.show()
        window.exec()

    def search_func(self):
        self.phonebook.clear()
        if self.search_line.text():
            for element in self.store.get_records(self.search_line.text()):
                self.phonebook.addItem(
                f'{element[0]} {element[1]}  —  {element[2]}  —  {element[3]}')
