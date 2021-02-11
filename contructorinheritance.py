class A:

    def __init__(self):
        print("Init A method")

    def feature1(self):
        print('Feature1 working')

    def feature2(self):
        print('Feature2 working')

class B(A):   #child class

    def __init__(self):
        super().__init__()          #it will print the both the classes
        print("Init B method")

    def feature3(self):
        print('Feature3 working')

    def feature4(self):
        print('Feature4 working')

a1=B()

