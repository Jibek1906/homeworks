# Github - Version Control System

class Animal:
    # Конструктор класса Animal
    def __init__(self, name, age):
        # Поля класса, с модификатором приватности __
        self.__name = name
        self.__age = age
        self.__was_born()  # Вызываем метод, который сообщает о рождении

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive integer")  # Генерируем ошибку при некорректном значении

    def set_name(self, name):
        self.__name = name

    # Геттер для имени
    def get_name(self):
        return self.__name

    # Геттер для возраста
    def get_age(self):
        return self.__age

    def info(self):
        return f'NAME: {self.__name}, AGE: {self.__age}, BIRTH YEAR: {2024 - self.__age}'

    # Приватный метод для вывода информации о рождении
    def __was_born(self):
        print(f'Animal {self.__name} was born.')

    # Абстрактный метод, который должен быть реализован в дочерних классах
    def make_voice(self):
        raise NotImplementedError('Method make_voice must be implemented.')


class Fish(Animal):
    def __init__(self, name, age):
        super(Fish, self).__init__(name, age)  # Инициализация родительского класса 2 вид

    def make_voice(self):
        pass


class Cat(Animal):
    def __init__(self, name, age):
        super(Cat, self).__init__(name, age)

    def make_voice(self):
        print('Meow')


class Dog(Animal):
    def __init__(self, name, age, commands):
        super(Dog, self).__init__(name, age)
        self.__commands = commands  # Приватное поле для команд собаки

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    # Переопределение метода info для добавления информации о командах
    def info(self):
        return super().info() + f', COMMANDS: {self.__commands}'

    def make_voice(self):
        print('Woof')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins):
        super(FightingDog, self).__init__(name, age, commands)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    # Переопределение метода info для добавления информации о победах
    def info(self):
        return super().info() + f', WINS: {self.__wins}'

    def make_voice(self):
        print('Rrr woof')

cat = Cat('Tom', 5)
dog = Dog('Snoopy', 3, 'Sit')
dog.commands = 'Sit, run'  # Изменение команды
fighting_dog = FightingDog('Reks', 1, 'Fight', 10)
fish = Fish('Dori', 2)

# Список всех животных
animals_list = [cat, fish, dog, fighting_dog]
for animal in animals_list:
    print(animal.info())  # Вывод информации о каждом животном
    animal.make_voice()
