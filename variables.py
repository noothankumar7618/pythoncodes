class Car:

    wheels=4           #class variables
    def __init__(self):
        self.mil=50            #instance variables
        self.com='BMW'

c1=Car()
c2=Car()

c1.mil=30 #updating new value

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
