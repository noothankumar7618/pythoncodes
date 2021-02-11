class A:

    def show(self):
        print("it is A")

class B(A):
    def show(self):
        print("it is B")

a1=B()
a1.show()