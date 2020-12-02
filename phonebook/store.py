import sqlite3
from phonebook.entities.record import Record


class Store:
    def __init__(self):
        self.connection = sqlite3.connect("phonebook.db")
        self.db = self.connection.cursor()
        self.db.execute("""create table if not exists Record (
            first_name text,
            last_name text,
            phone_number text UNIQUE,
            birth_date date
        )""")
        self.connection.commit()

    def add_record(self, record: Record):
        data = record.to_tuple()
        self.db.execute(
            f"""insert into Record 
            values ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}')""")
        self.connection.commit()

    def remove_record(self, first_name, last_name, phone_number):
        query = f"delete from Record where first_name = '{first_name}' and last_name = '{last_name}' and phone_number = '{phone_number}'"
        self.db.execute(query)
        self.connection.commit()

    def show_records(self):
        self.db.execute('select * from Record')
        return self.db.fetchall()
    
    def get_records(self, search_request):
        result = f"""select * from Record
        where 
            first_name like '%{search_request}%' or 
            last_name like '%{search_request}%' or
            phone_number like '%{search_request}%' or
            birth_date like '%{search_request}%'
        """
        data = self.db.execute(result).fetchall()
        return data

    def _key_exists(self, phone_number: str) -> bool:
        query = f"select 1 from Record where phone_number like '{phone_number}'"
        result = self.db.execute(query).fetchone()
        return result is not None

    def update_record(self, phone_number: str, new_record: Record):
        if phone_number != new_record.phone_number and self._key_exists(new_record.phone_number):
            raise ValueError("phone number already exists. Try new one.")
        query = """update Record
        set first_name = ?,
            last_name = ?,
            phone_number = ?,
            birth_date = ? 
        where
            phone_number = ?
        """
        self.db.execute(query, new_record.to_tuple() + (phone_number, ), )

    def get_record(self, phone_number: str) -> Record:
        result = f"select  first_name, last_name, phone_number, birth_date date from Record where phone_number like '{phone_number}'"
        data = self.db.execute(result).fetchone()
        return Record(*data)

    def close(self):
        self.connection.close()
