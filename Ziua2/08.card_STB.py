
## DEFINIRE
class STBCard:
    # Variabila Statica (apartine de clasa)
    RIDE = 3

    def __init__(self, titular="Nenominal", nr_calatorii=0, credit=0):
        self.titular = titular
        self.nr_calatorii = nr_calatorii
        self.credit = credit

    def validare(self):
        if self.nr_calatorii > 0:
            self.nr_calatorii -= 1
            print("Ai validat o calatorie")
        elif self.credit >= STBCard.RIDE:
            self.credit -= STBCard.RIDE
            print("Ai platit o calatorie noua")
        else:
            print("Ups, nu mai ai 3 lei pt o calatorie")

    def add_credit(self, suma):
        if suma > 0:
            self.credit += suma
            print(f"Ai incarcat suma {suma} lei.")
        else:
            print("Ups, nu ai incarcat nimic.")

    def add_calatorii(self, nr):
        if nr > 0:
            self.nr_calatorii += nr
            print(f"Ai pus {nr} calatorii.")
        else:
            print("Ups, ceva nu a mers.")

    def __str__(self):
        return f"Titular: {self.titular}\n Ai: {self.nr_calatorii} calatorii\n Ai: {self.credit} lei"
    


## FOLOSIRE
card = STBCard(titular="Ioana", nr_calatorii=15, credit=10)

print("Informatii card inainte de validare\n", card, "\n")

card.validare()
card.add_calatorii(5)
card.validare()

print("\nInformatii actuale")
print(card)