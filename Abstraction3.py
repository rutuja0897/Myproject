from abc import ABC,abstractmethod
class DefenceForce(ABC):

    def Gun(self):
        print("AK47")

    @abstractmethod
    def Area(self):
        pass

class Army(DefenceForce):
    def Area(self):
        print("Land")

class Airforce(DefenceForce):
     def Area(self):
         print("Sky")

class Navy(DefenceForce):
     def Area(self):
         print("Sea")


a=Army()
af=Airforce()
n=Navy()

a.Gun()
a.Area()

af.Gun()
af.Area()

n.Gun()
n.Area()