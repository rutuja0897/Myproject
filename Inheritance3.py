class A():
    def m1(self):
        print("This is class A method")

class B(A):
    def m2(self):
        print("This is class B method")
        super().m1()


bc=B()
bc.m2()
bc.m1()