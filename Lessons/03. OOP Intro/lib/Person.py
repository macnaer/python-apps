if __name__ == "__main__":
    Person


class Person:

    def __init__(self, name: str, surname: str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = age
        print("Constructor works")

    def show_person_info(self):
        print("Name: ", self.__name, "\nSurname: ",
              self.__surname, "\nAge: ", self.__age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if self.__age == new_age:
            print("The same age")
        elif self.__age > new_age:
            print("Error bad idea")
        elif new_age >= 120:
            print(self.__name, " can't live ", new_age, " years")
        else:
            self.__age = new_age
