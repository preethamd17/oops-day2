class Student:
    college_name = "ABC College"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    @staticmethod
    def is_pass(marks):
        return "Pass" if marks >= 35 else "Fail"

    def display(self):
        print(self.name, self.roll_no, Student.college_name)


s1 = Student("Ravi", 101)
s2 = Student("Anu", 102)

s1.display()
s2.display()

Student.change_college("XYZ College")

s1.display()
s2.display()

print(Student.is_pass(78))
print(Student.is_pass(30))
