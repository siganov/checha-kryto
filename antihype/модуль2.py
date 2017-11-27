class animal():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print('Имя: ', self.name,
        '\nвозраст: ', self.age)
class Уберменшь(animal):
    def кушат(self,y):
       if(isinstance(y, Унтерменшь)== 1):
            print("траль", self.name, " в возрасте", self.age,"затролeбасил", y.name)
            y.умират

class Унтерменшь(animal):
    def умират(self,y):
        del self

class дикая_киса(Уберменшь):
    pass

class негр(Унтерменшь):
    pass

y=негр("Рома***лалка", 5)
y.info()
x=дикая_киса("В@SЯH228",16)
x.info()
x.кушат(y)