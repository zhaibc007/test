from model import StudentModel


class StudentController:


    def __init__(self):

        self.__list_students = []
        self.__start_id = 1000

    @property
    def list_students(self):
        return self.__list_students

    def add_student(self, stu_target):

        stu_target.sid = self.__start_id
        self.__start_id += 1

        self.__list_students.append(stu_target)

    def remove_student(self, sid):

        stu = StudentModel(sid=sid)
        if stu in self.__list_students:
            # 需要重写StudentModel的__eq__方法
            self.__list_students.remove(stu)
            return True
        return False



    def update_student(self, stu_target):
        for stu in self.__list_students:
            if stu.sid == stu_target.sid:
                stu.sex = stu_target.sex
                stu.name = stu_target.name
                stu.age = stu_target.age
                stu.score = stu_target.score
                return True
        return False