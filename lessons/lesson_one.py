# python file - это модуль

class Transport:
    def __init__(self, the_model, the_year, the_color):
        # fields/attributes
        self.model = the_model  # attribute нужно создавать обязательно
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        print(f'Color changed to {self.color} to {new_color}')
        self.color = new_color

class Plane(Transport): # class один объектов сколько угодно
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)

class Car(Transport):
    counter = 0
    # constructor      #parametrs
    def __init__(self, the_model, the_year, the_color, penalties = 0): # init и self всегда здесь self через него предается адрес этого объекта
    # attribute нужно создавать обязательно
      # fields/attributes
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')

    def signal(self, num_of_times, sound):
        while num_of_times > 0:
            print(f'Car {self.model} is signaling {sound}')
            num_of_times -= 1
            
class Truck(Car):
    counter = 0
    def __init__(self, the_model, the_year, the_color, penalties = 0, load_capacity = 0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, weight, product_type):
        if weight > self.load_capacity:
            print(f'You can not load more tahan {self.load_capacity} kg.')
        else:
            print(f'You successfully loaded the cargo '
                  f'of {product_type} ({weight} kg.)')

print(f'Factory CAR produced: {Car.counter} car.')

number = 5
my_car = Car("Ford", "2021", "red", 40) # вызываем конструктор Car()
print(my_car) # ссылка объект
print(f'MODEL: {my_car.model}, YEAR: {my_car.year}, COLOR: {my_car.color}, PENALTIES: {my_car.penalties}')

my_car.drive("Osh")
my_car.drive("Tokmok")
my_car.drive("Bishkek")

best_car = Car(penalties=20, the_year="2024", the_model="bmw", the_color="red",)
print(best_car)
print(f'MODEL: {best_car.model}, YEAR: {best_car.year}, COLOR: {best_car.color}, PENALTIES: {best_car.penalties}')
# best_car.color = "Red"
best_car.change_color("Blue")
print(f'MODEL: {best_car.model}, YEAR: {best_car.year}, COLOR: {best_car.color}, PENALTIES: {best_car.penalties}')

print(f'Factory CAR produced: {Car.counter} cars.')

best_car.signal(3, 'Beep')

my_plane = Plane("Boeing", "2000", "white")
print(f'MODEL: {my_plane.model}, YEAR: {my_plane.year}, COLOR: {my_plane.color}')

truck = Truck("Volvo", "2019",
              "yellow", 200, 30000)
print(f'MODEL: {truck.model}, YEAR: {truck.year}, COLOR: {truck.color}, '
      f'PENALTIES: {truck.penalties}, LOAD CAPACITY: {truck.load_capacity}')
truck.load_cargo(50000, 'pears')
truck.load_cargo(25000, 'watermelon')

print(f'Factory Truck produced: {Truck.counter} trucks.')

print('End of the program')




