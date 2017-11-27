class крестовая_отвертка():
    def __init__(self):
        self.k=list()

    def  чечня(self,x):
        self.k.append(x)

    def лин(self):
        return len(self.k)

    def круто(self):
        return self.k[len(self.k)-1 ]

    def info(self):
        for i in range(0, len(self.k)):
            print(self.k[i])
        print("     ")

x=крестовая_отвертка()
x.чечня(2)
x.чечня(1)
x.чечня(4)
x.чечня(5)
x.info()
print(x.лин())
print(x.круто())