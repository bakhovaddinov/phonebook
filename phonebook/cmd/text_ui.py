while command != 'Exit':
    command = input('''Hello! 
    what do you wish to do?
    available options: 
    [1] Add a record
    [2] Deleate a record
    [3] Show the whole phonebook
    [4] Edit a record
    to exit print "Exit"\n ''')

    if command == '1':
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        phone = input('Enter your phone number: ')
        birth_date = date.fromisoformat(input('Enter your birth date: '))
        store = Store()
        store.add_record(Record(first_name, last_name, phone, birth_date))
        store.close()
    elif command == '2':
        first_name, last_name = input('Enter first name and last name: ').split(' ')
        store = Store()
        store.remove_record(first_name, last_name)
    elif command == '3':
        store = Store()
        store.output()