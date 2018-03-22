
class Konferencja:

    def __init__(self, nazwa, lokalizacja='Warszawa'):
        self.nazwa = nazwa
        self.lokalizacja = lokalizacja

    def say_hello(self):
        print('Hello from Konferencja {}'.format(self.nazwa))

    def __str__(self):
        return 'Nazwa konferencji: {}'.format(self.nazwa)


beIt = Konferencja(nazwa='BeIT')
beIt.say_hello()

print(beIt.__str__())
