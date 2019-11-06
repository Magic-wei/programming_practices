class Parent(object):
    def __init__(self):
        self.x = 1.0

    def function_x(self):
        print("Parent x:", self.x)

class Child1(Parent):
    def __init__(self):
        self.y = 2.0

    def function_y(self):
        print("Child1 y:", self.y)

class Child2(Parent):
    def __init__(self):
        super().__init__()
        self.y = 2.0

    def function_y(self):
        print("Child2 y:", self.y)

class Child3(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.y = 2.0

    def function_y(self):
        print("Child3 y:", self.y)

if __name__ == "__main__":
    P = Parent()

    C3 = Child3()
    C3.function_y()
    C3.function_x()

    C2 = Child2()
    C2.function_y()
    C2.function_x()

    C1 = Child1()
    C1.function_y()
    C1.function_x()  # return error


