from phonebook.design import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from phonebook.entities.record import Record
from phonebook.store import Store
from datetime import date
import sqlite3
from phonebook.input_window import DialogWindow

class MyWidget(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.store = Store()
        self.refresh()
        self.add_btn.clicked.connect(self.adding)
        self.rmv_btn.clicked.connect(self.remove)

    def adding(self):
        window = DialogWindow()
        window.show()
        window.exec()
        self.refresh()
    
    def refresh(self):
        self.phonebook.clear()
        for element in self.store.output():
            self.phonebook.addItem(f'{element[0]} {element[1]}  —  {element[2]}  —  {element[3]}')
    
    def remove(self):
        self.store = Store()
        data = self.phonebook.currentItem().text().split('  —  ')
        first_name, last_name = data[0].split()
        self.store.remove_record(first_name, last_name, data[1])
        self.refresh()
        
        
        




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())