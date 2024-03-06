
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f', Record Book: {self.record_book}'

class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < self.MAX_STUDENTS:
            self.group.add(student)
        else:
            raise ValueError('Досягнуто максимальну кількість студентів у групі.')

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove is not None:
            self.group.remove(student_to_remove)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

for i in range(10):
    gr.add_student(Student(f'Male{i}', 20+i, f'First{i}', f'Last{i}', f'AN{i}'))

try:
    gr.add_student(st1)
except ValueError as e:
    print(e)

print(gr)
