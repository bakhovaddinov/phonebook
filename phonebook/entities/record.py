
class Record:
    def __init__(self, first_name, last_name, phone_number, birth_date):
        if not self.is_valid_name(first_name):
            raise ValueError("first_name is incorrect")
        if not self.is_valid_name(last_name):
            raise ValueError("last_name is incorrect")
        if not self.is_valid_number(phone_number):
            raise ValueError("phone_number is incorrect")
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_date = birth_date

    def to_tuple (self):
        return (self.first_name, self.last_name, self.phone_number, self.birth_date.toString('MMMM d, yyyy'))

    def is_valid_name(self, name: str):
        if not name:
            return False
        if not name[0].isupper() or not name.replace(' ', '').isalnum():
            return False
        return True

    def is_valid_number(self, phone_number: str):
        if not phone_number:
            return False
        if not phone_number.isnumeric() or not phone_number[0] == '8':
            return False
        if len(phone_number) != 11:
            return False
        return True








