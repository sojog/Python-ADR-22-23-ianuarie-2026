import math

class Punct:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def muta_la_origine(self):
        self.x = 0
        self.y = 0

    def distanta(self, alt_punct):
        return math.sqrt((self.x - alt_punct.x) ** 2 + (self.y - alt_punct.y) ** 2) 



p1 = Punct(2, 3)
print(p1)

p1.muta_la_origine()
print(p1)

p2 = Punct(2, 3)
print(p1.distanta(p2))