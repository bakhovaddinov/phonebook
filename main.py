from classes import Name, Birthdate, Salary, PersonnelEntry, HRRegistry

registry = HRRegistry()
registry.add_entry(Name("John", "Romero"), 
                   Birthdate.from_string("1967/10/28"), 
		      Salary(50000))
registry.add_entry(Name("Edward", "Norton"), 
                   Birthdate.from_string("1969/08/18"), 
		      Salary(20000))
registry.add_entry(Name("Mary", "Sue"), 
                   Birthdate.from_string("1999/05/09"), 
		      Salary(300000))
registry.add_entry(Name("Walter", "White"), 
                   Birthdate.from_string("1959/09/07"), 
		      Salary(15000))
registry.delete_entry(
	registry.find_entry_by_name("Mary Sue")[0])
registry.delete_entry(
	registry.find_entry_by_name("Walter White")[0])
registry.add_entry(Name("Snake", "Plissken"), 
                   Birthdate.from_string("1981/07/10"), Salary(300))
registry.print_registry()
