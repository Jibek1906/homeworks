# Github - Version Control System

class Animal:
    # def info(self) : это сигнатруа метода
    def __init__(self, name, age):
        # поле
        self.__name = name # модификатор приватности __
        self.__age = age
        self.__was_born()

    def set_age(self, age): # set
        if type(age) == int and age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be an integer") # вызывает тип ошибки

    def set_name(self, name):
        self.__name = name

    def get_name(self): # get
        return self.__name

    def get_age(self):
        return self.__age

    def info(self):
        return f'NAME: {self.__name}, AGE: {self.__age}, BIRTH YEAR: {2024 - self.__age}'

    def __was_born(self):

class Cat(Animal):
    def __init__(self, name, age):
        # super().__init__(name, age)
        super(Cat, self).__init__(name, age) # второй способ

class Dog(Animal):
    def __init__(self, name, age, commands):
        super(Dog, self).__init__(name, age)
        self.__commands = commands

some_animal = Animal('Bob', 22)
some_animal.set_age(5)
print(some_animal.info())
print(some_animal.get_name())