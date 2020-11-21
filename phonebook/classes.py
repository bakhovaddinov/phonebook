class Name:
    def __init__(self, f_name, l_name):
        self.first_name = f_name # type: str
        self.last_name = l_name # type: str
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Salary:
    CURRENT_USD_TO_RUB = 61.73
    def __init__(self, value_in_dollars):
        self.value_in_dollars = value_in_dollars # type: float
    def to_rub(self):
        return self.value_in_dollars * Salary.CURRENT_USD_TO_RUB

class PersonnelEntry:
    def __init__(self, name, bdate, salary):
        self.name = name # type: Name
        self.bdate = bdate # type: Birthdate
        self.salary = salary # type: Salary

class Birthdate:
    def __init__(self, day, month, year):
        self.day = day # type: int
        self.month = month # type: int
        self.year = year # type: int
    def to_string(self, format="yyyy/mm/dd"):
        if format == "yyyy/mm/dd":
            return "{}/{}/{}".format(self.year, self.month, self.day)
        else:
            raise NotImplementedError

    @staticmethod
    def from_string(input_string, format="yyyy/mm/dd"):
        if format == "yyyy/mm/dd":
            year_str, month_str, day_str = input_string.split('/')
            year, month, day = (int(year_str), int(month_str), int(day_str))
            if Birthdate.is_date_valid(day, month, year):
                return Birthdate(day, month, year)
            else:
                raise RuntimeError
        else:
            raise NotImplementedError

    @staticmethod
    def is_date_valid(day, month, year):
        return True

class HRRegistry:
    def __init__(self):
        self._entries = {} # type: Dict[int, PersonnelEntry]
        self._uid_counter = 0 # type: int
    def add_entry(self, name, birthdate, salary):
        self._entries[self._uid_counter] = PersonnelEntry(name,
                                                       birthdate,
                                                       salary)
        self._uid_counter += 1

    def get_entries_count(self):
        return len(self._entries)

    def delete_entry(self, uid):
        if uid in self._entries:
            del self._entries[uid]
        else:
            raise RuntimeError
    def find_entry_by_name(self, name):
        for uid, entry in self._entries.items():
            if entry.name.get_full_name() == name:
                return uid, entry
        return None

    def print_registry(self):
        for uid, entry in self._entries.items():
            print("ID: {}\nName: {}\nBirthdate: {}\nSalary: {} RUB".format(uid,
                                                                       entry.name.get_full_name(),
                                                                       entry.bdate.to_string(),
                                                                       entry.salary.to_rub()))
            print()



