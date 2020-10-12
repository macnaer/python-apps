from lib.Person import Person


bill = Person("Bill", "Gates", 59)
bill.show_person_info()
print("Getter age: ", bill.age)
bill.age = 120
bill.show_person_info()
