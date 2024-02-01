# créé par Leonel Akio Briones et Hanfei Chen

import random
from colorama import init, Fore

# Initialiser colorama pour avoir un output lisible
init(autoreset=True)

# Définir la classe NPC
class NPC:
    def __init__(self, nom, race, espèce, profession):
        self.nom = nom
        self.race = race
        self.espèce = espèce
        self.profession = profession

        # Initialisation des caractéristiques avec des dés
        self.force = self._lancer_des(4, 6)
        self.agilité = self._lancer_des(4, 6)
        self.constitution = self._lancer_des(4, 6)
        self.intelligence = self._lancer_des(4, 6)
        self.sagesse = self._lancer_des(4, 6)
        self.charisme = self._lancer_des(4, 6)

        # Initialisation de la classe d'armure et des points de vie
        self.classe_armure = self._lancer_des(2, 12)
        self.points_de_vie = self._lancer_des(2, 20)



    def _lancer_des(self, nb_des, faces):
        # Simulation d'un lancer de dés classique
        return sum(sorted([random.randint(1, faces) for _ in range(nb_des)])[1:])

    def afficher_caracteristiques(self):
        # Affichage des caractéristiques du NPC
        print(f"{Fore.GREEN}Nom: {self.nom}")
        print(f"Race: {self.race}")
        print(f"Espèce: {self.espèce}")
        print(f"Profession: {self.profession}")
        print(f"Force: {self.force}")
        print(f"Agilité: {self.agilité}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Sagesse: {self.sagesse}")
        print(f"Charisme: {self.charisme}")
        print(f"Classe d'armure: {self.classe_armure}")
        print(f"Points de vie: {self.points_de_vie}")

# Définir la classe Kobold, sous-classe de NPC
class Kobold(NPC):
    def attaquer(self, cible):
        print(f"{Fore.RED}{self.nom} attaque {cible.nom}!")

    def subir_dommage(self, quantite):
        quantite_apres_reduction = max(quantite - self.classe_armure, 0)
        print(f"{Fore.RED}{self.nom} subit {quantite_apres_reduction} points de dommage!")
        self.points_de_vie -= quantite_apres_reduction

# Définir la classe Heros, sous-classe de NPC
class Heros(NPC):
    def attaquer(self, cible):
        print(f"{Fore.BLUE}{self.nom} attaque {cible.nom}!")

    def subir_dommage(self, quantite):
        des = random.randint(1,20)
        if des != (20):
            quantite_apres_reduction = max(quantite - self.classe_armure, 0)
            print(f"{Fore.BLUE}{self.nom} subit {quantite_apres_reduction} points de dommage!")
            self.points_de_vie -= quantite_apres_reduction
        elif des == (1):
            print(f"{Fore.GREEN} Le coup n'as pas fonctionné")
        else:
            quantite_apres_reduction = (quantite)
            print(f"{Fore.YELLOW}{self.nom} subit une attaque critical avec {quantite_apres_reduction} points de dommage!")
            self.points_de_vie -= quantite_apres_reduction

# Définir la classe des_20_faces
class Des20Faces:
    def __init__(self, heros, kobold):
        self.heros = heros
        self.kobold = kobold

    def d20(self, adversaire):
        des = random.randint(1, 20)
        d8 = random.randint(1, 8)

        if des == 1:
            return 0, False
        elif des == 20:
            return d8, True
        else:
            armor_class = self.heros.classe_armure if adversaire == "heros" else self.kobold.classe_armure

            if adversaire == "heros" and des >= armor_class:
                return max(des, 0), False
            elif adversaire == "kobold" and des >= armor_class:
                return max(des, 0), False

            return 0, False

# Exemple d'utilisation
kobold = Kobold(nom="Kobold1", race="Kobold", espèce="Reptile", profession="Guerrier")
heros = Heros(nom="Héros1", race="Humain", espèce="Humanoid", profession="Paladin")
des = Des20Faces(heros, kobold)

kobold.afficher_caracteristiques()
heros.afficher_caracteristiques()

kobold.attaquer(heros)
damage, is_critical = des.d20("heros")

heros.subir_dommage(damage)
