
class Record:
    def __init__(self, first_name, last_name, phone_number, birth_date):
        if not self.is_valid_name(first_name):
            raise ValueError('''The first_name is incorrect 
        \nthe first letter should be capital
        \nalso don't use '—' ''')
        if not self.is_valid_name(last_name):
            raise ValueError('''The last_name is incorrect 
        \nthe first letter should be capital
        \nalso don't use '—' ''')
        if not self.is_valid_number(phone_number):
            raise ValueError('''The phone_number is incorrect
        \nit should start with '+7' or '8' and 10 more numbers ''')
        self.first_name = first_name.replace('—','')
        self.last_name = last_name.replace('—','')
        self.phone_number = phone_number.replace('+7', '8')
        self.birth_date = birth_date

    def to_tuple(self):
        return (self.first_name, self.last_name, self.phone_number, self.birth_date.toString('MMMM d, yyyy'))

    def is_valid_name(self, name: str):
        if not name:
            return False
        if not name[0].isupper() or not name.replace(' ', '').isalnum():
            return False
        return True

    def is_valid_number(self, phone_number: str):
        phone_number = phone_number.replace('+7', '8')
        if not phone_number:
            return False
        if not phone_number.isnumeric() or not phone_number[0] == '8':
            return False
        if len(phone_number) != 11:
            return False
        return True
