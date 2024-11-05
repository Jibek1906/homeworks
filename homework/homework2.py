class Figure:

    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):

    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        return f"Square with side length: {self.__side_length} {self.unit}, Area: {self.calculate_area()} {self.unit}"

class Rectangle(Figure):

    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        return f"Rectangle with side length: {self.__length} {self.unit} , width: {self.__width} {self.unit}, Area: {self.calculate_area()} {self.unit}"

square = Square(5)
square2 = Square(8)


rectangle = Rectangle(2, 4)
rectangle2 = Rectangle(9, 5)
rectangle3 = Rectangle(6, 10)

figures_list = [square, square2, rectangle, rectangle2, rectangle3]
for figure in figures_list:
    print(figure.info())