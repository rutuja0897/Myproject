a,b=15,20
class A:
    a,b=10,20

class B(A):
    a,b=100,200
    def m1(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(super().a+super().b)
        print(globals()['a']+globals()['b'])

b1=B()
b1.m1(1,2)