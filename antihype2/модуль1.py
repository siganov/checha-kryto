class Моряк:
    def бабло(self):
        pass
class Боцман(Моряк):
    def __init__(self,x):
        self.x=x
    def бабло(self):
        print(self.x*20.8*8)
class Юнга(Моряк):
    def __init__(self,y):
        self.y=y
    def бабло(self):
       return(self.y)
a=Боцман(10)
a.бабло()


