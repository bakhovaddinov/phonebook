import sqlite3
from phonebook.entities.record import Record


class Store:
    def __init__(self):
        self.connection = sqlite3.connect("phonebook.db")
        self.base = self.connection.cursor()
        self.base.execute("""create table if not exists Record (
            first_name text UNIQUE,
            last_name text,
            phone_number text,
            birth_date date
        )""")
        self.connection.commit()

    def add_record(self, record: Record):
        self.base.execute(
            'insert into Record values (?, ?, ?, ?)', record.to_tuple())
        self.connection.commit()

    def remove_record(self, first_name, last_name, phone_number):
        query = f"delete from Record where first_name = '{first_name}' and last_name = '{last_name}' and phone_number = '{phone_number}'"
        self.base.execute(query)
        self.connection.commit()

    def get_records(self):
        self.base.execute('select * from Record')
        return self.base.fetchall()

    def close(self):
        self.connection.close()
