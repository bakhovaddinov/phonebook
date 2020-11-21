from phonebook.entities.record import Record
from phonebook.store import Store
from datetime import date

command = input('Do you wish to add a record? [y/n]')

if command == 'y':
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    phone = input('Enter your phone number: ')
    birth_date = date.fromisoformat(input('Enter your birth date: '))
    store = Store()
    store.add_record(Record(first_name, last_name, phone, birth_date))
    store.close()
