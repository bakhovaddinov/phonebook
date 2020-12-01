import sqlite3
from phonebook.entities.record import Record


class Store:
    def __init__(self):
        self.connection = sqlite3.connect("phonebook.db")
        self.base = self.connection.cursor()
        self.base.execute("""create table if not exists Record (
            first_name text,
            last_name text,
            phone_number text unique,
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

    def show_records(self):
        self.base.execute('select * from Record')
        return self.base.fetchall()
    
    def get_records(self, search_request):
        result = """select * from Record
        where 
            first_name like '%?%' or 
            last_name = '%?%' or
            phone_number = '%?%' or
            birth_date = '%?%' 
        """
        requests = (search_request, search_request, search_request, search_request, )
        print(requests)
        return self.base.execute(result, requests, ).fetchall()


    def update_record(self, phone_number: str, new_record: Record):

        query = """update Record
        set first_name = ?,
            last_name = ?,
            phone_number = ?,
            birth_date = ? 
        where
            phone_number = ?
        """
        self.base.execute(query, new_record.to_tuple() + (phone_number, ), )

    def close(self):
        self.connection.close()
