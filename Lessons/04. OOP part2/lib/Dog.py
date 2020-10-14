if __name__ == "__main__":
    Dog


class Dog:
    def __init__(self, name: str, breed: str, age: int, color: str, gender: str):
        self._name = name
        self._breed = breed
        self._age = age
        self._color = color
        self._gender = gender
        print("Dog Constructor ", self._name)

    def dog_info(self):
        print("==================================", "\nName: ", self._name, "\nBreed: ", self._breed,
              "\nAge: ", self._age, "\nColor: ", self._color, "\nGender: ", self._gender)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name.lower() == "con":
            print("\n *****Wrong name*******")
        else:
            self._name = new_name

    def __del__(self):
        print("Dog Destructor ", self._name)
