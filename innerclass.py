class Student:     #outer class

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:    #inner class

        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand,self.ram,self.cpu)

s1=Student('Noothan',564)
s2=Student('Harshith',675)

s1.show()
