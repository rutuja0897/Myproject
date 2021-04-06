class Myclass:
    __empid=101
    def getempid(self,eid):
        self.__empid=eid

    def dispempid(self) -> object:
        print(self.__empid)


obj=Myclass()
#obj.getempid(105)
obj.dispempid()