class Myclass:
    __empid=101

    def getempid(self,eid):
        self.__empid=eid

    def dispempid(self):
        print(self.__empid)

obj=Myclass()
obj.dispempid()

