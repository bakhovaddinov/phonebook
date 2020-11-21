import sqlite3
from phonebook.entities.record import Record

class Store:
    def __init__(self):
        self.connection = sqlite3.connect("phonebook.db")
        self.connection.execute("""create table if not exists Record (
            first_name text,
            last_name text,
            phone_number text,
            birth_date date
        )""")
        self.connection.commit()

    def add_record(self, record: Record):
        self.connection.execute('insert into Record values (?, ?, ?, ?)', record.to_tuple())
        self.connection.commit()

    def remove_record(self, f_name, l_name):
        self.connection.execute('delete from Record where first_name = f_name and last_name = l_name')

    def close(self):
        self.connection.close()

