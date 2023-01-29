class Student:
    # static variable
    school = "Himacha"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3



    @classmethod
    def info(cls):
        return cls.school

    
    def info2():
        print("this is static methid .. .. ")




s1 = Student(12,32,44)
s2 = Student(44,75,66)

print(s2.avg())
print(Student.info())
print(Student.info2())