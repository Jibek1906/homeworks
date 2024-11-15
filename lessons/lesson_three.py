# __ модификация
# множественное наследование
# магические методы - потому что запускаются не явным образом,вызываем не по названию, а они выполняются автоматически в определенный момент
# распечатка индекса идет от класса изначального object <class 'object'>
# методы бывают - магическими, обычными, классовыми и статичными
# посмотреть обычные и классовые методы разница
# статичные методы - это будто обычная функция вложена в класс не взаимодействуют с объектами класса и аттрибутами класса
# суть ООП в том, что объекты взаимодействуют друг с другом  на основе адресов

class Calculator:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property # декоратор
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

class Car:
    def __init__(self, model, year, owner):
        self.__model = model
        self.__year = year
        if type(owner) == Person: # без этого будет просто записываться в srting, обязываем принимать объект сложного типа данных person
            self.__owner = owner

    @property
    def model(self): # в других классах обращаемся к model, а не к __model
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    def drive(self):
        print(f'Car {self.__model} is driving.')

    def __str__(self): # магический метод Простыми словами, __str__ — это метод, который говорит Python, как представить объект в виде строки. Когда мы вызываем print() на объекте, Python смотрит, есть ли у него метод __str__, и если да, использует его, чтобы понять, что выводить.
        return f'MODEL: {self.__model}, YEAR: {self.__year} OWNER: {self.__owner.name}' # будет робать у всех наследуемых классов, но только выодить точно так же, как здесь, чтобы получить другой результат переопределяем внутри дочерних классов

    def __lt__(self, other): # lower than
        return self.__year < other.__year # __year обращаемся напрямую, year через getter

    def __gt__(self, other): # greater than
        return self.__year > other.__year

    def __eq__(self, other): # equal
        return self.__year == other.__year

    def __ne__(self, other): # not egual
        return self.__year != other.__year

    def __le__(self, other): # less or equal
        return self.__year <= other.__year

    def __ge__(self, other): # greater or equal
        return self.__year >= other.__year

class FuelCar(Car):
    __total_fuel = 0

    @staticmethod
    def get_fuel_type():
        return 'AI - 95'

    # в cls автоматически передается адрес класса
    @classmethod  # работают с классовыми аттрибутами, либо с другими классовыми методами, но не имеет никакой связи к аттрибутам объекта после self и также к методам относящимся к объектам
    def buy_fuel(cls, amount):
        cls.__total_fuel += amount
        print(cls.print_total_fuel())

    @classmethod
    def print_total_fuel(cls):
        print(f'Factory FUEL_CAR has {cls.__total_fuel} litter.')

    def __init__(self, model, year, fuel_bank, owner):
        # super().__init__(model, year)
        # super(FuelCar, self).__init__(model, year)
        Car.__init__(self, model, year, owner) # третий метод удобен при множественном наследовании
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel.') # обращаемся к геттеру model

    def __str__(self):
        return super().__str__() + f', FUEL BANK: {self.__fuel_bank}' # переопределяем

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank

class ElectricCar(Car):
    def __init__(self, model, year, battery, owner):
        Car.__init__(self, model, year, owner)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by battery.') # обращаемся к геттеру model

    def __str__(self):
        return super().__str__() + f', BATTERY: {self.__battery}'

class HybridCar(ElectricCar, FuelCar): # приоритет будет у первого прописанного класса
    def __init__(self, model, year, fuel_bank, battery, owner):
        FuelCar.__init__(self, model, year, fuel_bank, owner)
        ElectricCar.__init__(self, model, year, battery, owner)

# some_car = Car('Audi', 2000)
# print(some_car) без метода __str__ выведет адрес объекта в памяти

FuelCar.buy_fuel(500) # при выозове self он будет принимать новое значение, так как был вызван не через объект, а через название класса

my_friend = Person('Jim', 30)

fuel_car = FuelCar('Audi A8', 2020, 75, my_friend)
print(fuel_car)

electric_car = ElectricCar('Tesla Model X', 2024, 25000, my_friend)
print(electric_car)

# p = Person('Bob', 26)
# a = b

hybrid_car = HybridCar('Toyota Prius', 2021, 60, 15000, Person('Bob', 26))
print(hybrid_car)
hybrid_car.drive() # при наследовании будет наследовать приорететно первый класс(FuelCar, ElectricCar) Car {self.__model} is driving by fuel

print(HybridCar.mro()) # метод покажет по какой очередности действует приоретет

number_1 = 2
number_2 = 10
print(f'Number one is bigger than number two: {number_1 > number_2}')
print(f'Number one is smaller than number two: {number_1 < number_2}')
print(f'Fuel car is worse than hybrid car: {fuel_car < hybrid_car}')
print(f'Electric car is better than hybrid car: {electric_car > hybrid_car}')
print(f'Electric car is the same with hybrid car: {electric_car == hybrid_car}')

print(fuel_car + hybrid_car)

# FuelCar.__total_fuel -= 100
FuelCar.print_total_fuel()
print(f'Factory FUEL_CAR uses {FuelCar.get_fuel_type()} fuel.')


print(f'Owner of prius was born in {2024 - hybrid_car.owner.age}.')

print(HybridCar.mro) # покажет очередность приорететов [<class '__main__.HybridCar'>, <class '__main__.ElectricCar'>, <class '__main__.FuelCar'>, <class '__main__.Car'>, <class 'object'>]

# первй приоритет перед классом это object
