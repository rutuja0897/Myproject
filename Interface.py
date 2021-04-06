from abc import ABC, abstractmethod
class Defenceforce(ABC):
    @abstractmethod
    def Gun(self):
        pass
    def Area(self):
        pass

class Army(Defenceforce):
     def Gun(self):
         print("AK41")

     def Area(self):
         print("Land")

class Airforce(Defenceforce):
      def Gun(self):
          print("AK42")

      def Area(self):
          print("Sky")

class Navy(Defenceforce):
     def Gun(self):
         print("AK43")

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
