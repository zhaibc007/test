class StudentModel:


    def __init__(self, name="", sex="", score=0.0, age=0, sid=0):
        self.name = name
        self.sex = sex
        self.score = score
        self.age = age
        self.sid = sid

    def __str__(self):
        return f"{self.name} your account is {self.sid},age is {self.age},movie name is {self.sex},movie score is {self.score}"

    def __eq__(self, other):
        return self.sid == other.sid