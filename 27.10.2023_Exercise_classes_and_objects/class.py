class Class:
    students = []
    grades = []

    def __init__(self, name):
        self.name = name
        self.__students_count = 22

    def add_student(self, name: str, grade: float):
        pass

    def get_average_grade():
        pass

    def __repr__(self):
        return f"The students in {class_name}: {students}. Average grade: {average_grade}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)