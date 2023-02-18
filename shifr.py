from random import randint
class F():
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    def __in_method(self):
        self.operation = randint(1, 2)
        if self.operation == 1:
            return self.__a + self.__b
        elif self.operation == 2:
            return self.__a - self.__b
    def printer(self):
        print(self.__in_method())

ob = F(10, 15)
ob.printer()