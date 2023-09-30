
# class DemoClass:
#     def __init__(self):
#         print("gasdhashdahsdhasdh")

    
#     def student_details(self, name, course, grade):
#         self.name = name
#         self.course = course
#         self.grade = grade

#         message = f"STUDENT NAME: {self.name}\nCourse: {self.course}\nGrade: {self.grade}"
#         print(message)



# my_demo = DemoClass()
# my_demo2 = DemoClass()
# my_demo3 = DemoClass()

# my_demo.student_details("Joel", "BSIT", 80)
# my_demo2.student_details("Hello", "BSIT", 90)
# my_demo3.student_details("World", "BSIT", 88)


class Student:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email


    def get_name(self):
        return self.name
    

    def get_address(self):
        return self.address
    

    def get_umail(self):
        return self.email


student_list: list[Student] = []

while True:
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    email = input("Enter your email: ")

    new_student = Student(name, address, email)
    student_list.append(new_student)

    for student in student_list:
        print(student.get_name())
