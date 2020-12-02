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
        data = record.to_tuple()
        self.base.execute(
            f'insert into Record values ({data[0]}, {data[1]}, {data[2]}, {data[3]})', record.to_tuple())
        self.connection.commit()

    def remove_record(self, first_name, last_name, phone_number):
        query = f"delete from Record where first_name = '{first_name}' and last_name = '{last_name}' and phone_number = '{phone_number}'"
        self.base.execute(query)
        self.connection.commit()

    def show_records(self):
        self.base.execute('select * from Record')
        return self.base.fetchall()
    
    def get_records(self, search_request):
        result = f"""select * from Record
        where 
            first_name like '%{search_request}%' or 
            last_name like '%{search_request}%' or
            phone_number like '%{search_request}%' or
            birth_date like '%{search_request}%'
        """
        data = self.base.execute(result).fetchall()
        return data

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
