if __name__ == "__main__":
    HunterDog

from lib.Dog import Dog


class Test:
    def __init__(self):
        print("Test constructor")


class HunterDog(Dog):
    def __init__(self, name, breed, age, color, gender, speed: int):
        super().__init__(name, breed, age, color, gender)
        self.__speed = speed
        print("HunterDog Constructor ")

    def dog_info(self):
        print("==================================", "\nName: ", self._name, "\nBreed: ", self._breed,
              "\nAge: ", self._age, "\nColor: ", self._color, "\nGender: ", self._gender, "\nSpeed: ", self.__speed)

    def dog_hunt(self):
        print(self._name, " is hunting...")
        self.__speed -= 30
        if self.__speed <= 40:
            self.__dog_rest()

    def __dog_rest(self):
        self.__speed = 100

    def __del__(self):
        print("HunterDog Destructor ")
