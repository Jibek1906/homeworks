class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'My full name is {self.full_name} and age is {self.age}. Marriage status: {self.is_married}')


class Student(Person):

    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks if marks is not None else {}

    def introduce_myself(self):
        super().introduce_myself()
        print('My marks:')
        for key, value in self.marks.items():
            print(f'{key}: {value}')

    def average_grade(self):
        total = sum(self.marks.values())
        average = total / len(self.marks.keys())
        print(f'Average grade: {average}')

class Teacher(Person):

    base_salary = 50000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name,age,is_married)
        self.experience = experience

    def teacher_salary(self):
        salary = Teacher.base_salary
        for year in range(4, self.experience + 1):
            if year > 3:
                salary *= 1.05
        print(f'{self.full_name} salary is {salary}')


teacher1 = Teacher('Irshad Imtyaz', 35, True, 6)
print(f'Teacher full name: {teacher1.full_name}, age: {teacher1.age}, is_married: {teacher1.is_married}')
teacher1.teacher_salary()

def create_students():
    students = []
    students.append(Student('Amalia', 19, True, {'Math': 4, 'History': 3, 'Music': 5, 'Geography': 3}))
    students.append(Student('Aid', 16, False, {'Math': 4, 'PE': 3, 'Music': 5}))
    students.append(Student('Silvester', 20, False, {'Math': 5, 'PE': 5, 'Music': 4, 'Russian': 4, 'English': 5}))
    return students

students = create_students()
for student in students:
    student.introduce_myself()
    student.average_grade()

