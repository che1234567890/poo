class StringFoo:
    def __init__(self):
        self.string = None
    def set_string(self):
        self.string = input()


    def print_string(self):
        print((self.string).upper())

obj = StringFoo()
obj.set_string()
obj.print_string()

class Rectangle:
    def __init__(self, largeur, longeur):
        self.largeur = largeur
        self.longeur = longeur

    def calcul_air(self):
        self.air = self.largeur * self.longeur

    def afficher_infos(self):
        print("l'aire du rectangle est ", self.air)

rectangle = Rectangle(10, 12)
rectangle.calcul_air()
rectangle.afficher_infos()

from math import pi

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        calculate = self.rayon ** 2 * pi
        print("l'aire du cerlce est ", calculate)
    def calcul_circonference(self):
        calculate = pi * self.rayon * 2
        print("la circonference du cerlce est ", calculate)

cercle = Cercle(8)
cercle.calcul_aire()
cercle.calcul_circonference()

from random import randint

class Hero:
    def __init__(self, link):
        self.hp = randint(2,10)
        self.ap = randint(1,6)
        self.df = randint(1,6)
        self.name = link

    def attaque(self):
        attaque = randint(1,6) + self.ap
        return attaque
    def dommage(self, dommage):
        self.hp -= dommage - self.df
        print("hp de link: ", self.hp)

    def est_vivant(self):
        if self.hp <= 0:
            False
        else:
            True

Hero = Hero("link")
print(Hero.attaque())
Hero.dommage(1)
Hero.est_vivant()
