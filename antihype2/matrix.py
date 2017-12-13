from random import randint
def matrix(boo,size):
    if boo == True:
        diap = int(input("Введите диапазон: "))
        m = [[int(randint(10,diap)) for i in range(size)] for j in range(size)]
        return m
    else:
        m = [[int(input()) for i in range(size)] for j in range(size)]
        return m

class square_matrix:
    n = 0
    def __init__(self, size, boo):
        self.size = size
        self.boo = boo
        self.m = matrix(boo,size)
        self.s = 0
        square_matrix.n += 1
        #print(self.m)

#2. Размер и кол-во матриц
    def get_inform(self):
        return self.size, square_matrix.n
    x = property(get_inform)

#3. Вывод таблицей
    def __str__(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.m[i][j], end=" ")
            print()

#4. Главная диагональ
    def main_diagonal(self):
        d = 0
        for i in range(self.size):
            d += self.m[i][i]
        print("Главная диагональ: ", d)

#5. Транспонирование
    def transposition(self):
        new = [[0 for i in range(self.size)] for j in range(self.size)]
        print("\nТранспонирование:")
        for i in range(self.size):
            for j in range(self.size):
                new[i][j] = self.m[j][i]
                self.s += self.m[i][j]
                print(new[i][j], end=" ")
            print()

#5. Сравнение
    def __lt__(self, other):
        if self.s < other.s:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.s == other.s:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.s > other.s:
            return True
        else:
            return False

#6. Сложение матриц
    def qwe(self,other):
        summa = []
        if self.size == other.size:
            for i in range(self.size):
                for j in range(self.size):
                    summa[i][j] = self.m[i][j] + other.m[i][j]
                    print(summa[i][j], end=" ")
                print()

a = square_matrix(5, True)
b = square_matrix(5, True)
print(a.x)
print(b.x)
a.main_diagonal()
b.main_diagonal()
a.transposition()
b.transposition()

print("\nA больше B? ",a > b)
print("A меньше B? ",a < b)
print("A равно B? ",a == b)
konec = input("end")
a.qwe(b)
konec = input("end")
