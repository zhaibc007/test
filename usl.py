from bll import StudentController
from model import StudentModel


class StudentView:


    def __init__(self):
        self.__controller = StudentController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1. Add movie information")
        print("2. Show movie information")
        print("3. Delete movie information")
        print("4. Modify movie information")

    def __select_menu(self):
        item = input("Please enter your options：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__change_student()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("please input your name as userID：")
        stu.sex = input("please input movie name：")
        stu.score = int(input("please input your score about this movie："))
        stu.age = int(input("please input your age："))
        self.__controller.add_student(stu)

    def __display_students(self):
        for stu in self.__controller.list_students:
            print(stu)
            # print(f"{stu.name}的编号是{stu.sid},年龄是{stu.age},性别是{stu.sex},成绩是{stu.score}")

    def __delete_student(self):
        sid = int(input("Please input the userID you waant to be deleted："))
        if self.__controller.remove_student(sid):
            print("success")
        else:
            print("fail")

    def __change_student(self):
        stu = StudentModel()
        stu.sid = int(input("please input userID you want to modify："))
        stu.name = input("please input your modify name：")
        stu.sex = input("please input modify movie name：")
        stu.score = int(input("please input modify movie score："))
        stu.age = int(input("please input modify age："))
        if self.__controller.update_student(stu):
            print("modify success")
        else:
            print("modify fail")