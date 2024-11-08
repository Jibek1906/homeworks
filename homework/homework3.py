class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        total_memory = self.memory + self.cpu
        return total_memory

    def __str__(self):
        return f'Информация о компьютере: CPU: {self.__cpu}, Память: {self.__memory}'

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list if sim_cards_list is not None else []

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {self.__sim_cards_list[sim_card_number - 1]}')

    def __str__(self):
        return f'Телефон с сим-картами: {self.__sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'Построение маршрута до {location}...')

    def __str__(self):
        return f'{Computer.__str__(self)}, {Phone.__str__(self)}'

computer = Computer(cpu=4, memory=16)
phone = Phone(sim_cards_list=["Beeline", "MegaCom"])
smartphone1 = SmartPhone(cpu=6, memory=32, sim_cards_list=["Beeline", "MegaCom"])
smartphone2 = SmartPhone(cpu=8, memory=64, sim_cards_list=["MegaCom", "O!"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print("\nИспользование методов:")
print("Computer make_computations:", computer.make_computations())
phone.call(1, '+996 778 95 86')
smartphone1.use_gps("Алматы")

print("\nСравнение объектов Computer:")
print("computer == smartphone1:", computer == smartphone1)
print("computer != smartphone1:", computer != smartphone1)
print("computer < smartphone1:", computer < smartphone1)
print("computer > smartphone1:", computer > smartphone1)
print("computer <= smartphone1:", computer <= smartphone1)
print("computer >= smartphone1:", computer >= smartphone1)