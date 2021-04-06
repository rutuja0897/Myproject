class P:
    def Property(self):
        print("cash+land+gold+power")

    def marry(self):
        print('tina')

class C(P):
    def Power(self):
        print('power')
    def marry(self):
        super().marry()
        print('Katrina')

c=C()
c.marry()
c.Property()