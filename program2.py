class School:
    def school_details(self):
        print("School Name: Royal English School")
        print("School Marks: 74%")


class College:
    def college_details(self):
        print("College Name: Gopalan College")
        print("College Marks: 90%")


class Student(School, College):
    def student_details(self):
        print("Student Name: Sanjana")
        print("Department: ISE")


S1 = Student()

S1.student_details()
S1.school_details()
S1.college_details()



