class Students:
    school='Digi Learn Commnuity'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod    #decorators (classic method)
    def info(self):
        return self.school

    @staticmethod    #decorators (static method)
    def info1():
        print("hey what are you doing here")

s1=Students(12,34,56)
s2=Students(13,67,97)

print(s2.avg())
print(Students.info())  #to display school name (classic method)
Students.info1()        #to display school name (static method)

