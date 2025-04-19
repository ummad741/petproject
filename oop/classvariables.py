# classvariable see it here -> images/classvariable.png

class Student:
    # class variable butun classga tegishli umumiy hotira
    school_name = "ABZ-school"  # class method

    # har bir object uchun
    def __init__(self, name: str, age: int):
        self.name = name  # instance variable
        self.age = age
        print(self.school_name)  # accessing


s1 = Student('test', 20)
print(s1.school_name)  # accsessing
s1.school_name = "XBZ-school"  # modify
print(s1.school_name)


class Course:
    # class variable
    course = "Python"

class Student(Course):
    # class variable
    course = "SQL"

    def __init__(self, name):
        super().__init__()
        self.name = name

    def show_student(self):
        # Accessing class variable
        print('Before')
        print("Student name:", self.name, "Course Name:", self.course)
        # changing class variable's value
        print('Now')
        self.course = "Machine Learning"
        print("Student name:", self.name, "Course Name:", self.course)

# creating object of Student class
stud = Student("Emma")
stud.show_student()

# parent class course name
print('Parent Class Course Name:', Course.course)