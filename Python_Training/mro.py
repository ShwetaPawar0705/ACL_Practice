# MRO: Used to determine the order in which classes are searched when calling a method(function with object). Used in multilevel inheritance.

class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):
    pass

d = D()
d.method()

print(D.mro())  # sequence to search

'''Why does B come before C?
the order of inheritance matters so B is given more priority than C'''