class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'Name: {self.__name}, Age: {self.__age}'

if __name__ == '__main__': #Эта конструкция является стандартным способом защитить часть кода от выполнения, если модуль импортируется в другой скрипт.
    # Если вы импортируете этот модуль в другой файл, например:
    # import your_module_name
    # то код внутри if __name__ == '__main__': не будет выполнен. Это защищает вашу программу от выполнения нежелательных действий при использовании как библиотеки.
    # __name__ зарезервированная пременная в python
    person = Person('John', 23)
    print(person)