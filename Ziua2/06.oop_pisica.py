
## Definire a logicii
class Pisica:
    # "__" -> functii magice 
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def miauna (self):
        print(self.nume, "face Miau Miau Miau")

    def categorie_varsta(self):
        if self.varsta < 3:
            print("Pisica", self.nume,  "este tinerica")
        else:
            print("Pisica", self.nume,  "este batranica")



# Folosire a logicii 
tom = Pisica("Tom", 1)
tom.miauna()

tom.categorie_varsta()

rino = Pisica("Rino", 6)
rino.miauna()

rino.categorie_varsta()