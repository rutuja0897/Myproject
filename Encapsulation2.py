class Myclass:
    def __disp1(self):
        print("This is private method")

    def disp2(self):
        print("This is simple or concrete method")
        self.__disp1()


obj=Myclass()
obj.disp2()