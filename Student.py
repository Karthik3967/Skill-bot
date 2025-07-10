class Student:
    def _init_(self,name=None,marks=0):
        self.__name=name
        self.__marks=marks

    def setName(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setmarks(self,marks):
            self.__marks=marks
    def getmarks(self):
        if marks < 0 or marks > 100:
            return "Marks must be between 0 and 100"
        else:
            self.__marks = marks

        return self.__marks

student=input("Student name : ")
marks=int(input("Student marks : "))
stu=Student()
stu.setName(student)
stu.setmarks(marks )
print(stu.getname())
print(stu.getmarks())