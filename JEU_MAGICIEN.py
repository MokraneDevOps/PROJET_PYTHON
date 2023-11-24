#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      mokrane
#
# Created:     17/11/2023
# Copyright:   (c) mokrane 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


class Personnage:
    def __init__(self, nom, vie, force=0, endurance=0, rapidite=0, intelligence=0):
        self.Nom = nom
        self.Vie = vie
        self.Force = force
        self.Endurance = endurance
        self.Rapidite = rapidite
        self.Intelligence = intelligence

    def afficher_info(self):
        print(f"Nom: {self.Nom}, Vie: {self.Vie}, Force: {self.Force}, Endurance: {self.Endurance}, Rapidite: {self.Rapidite}, Intelligence: {self.Intelligence}")

    def est_en_vie(self):
        if self.Vie > 0:
            print(f"Il reste {self.Vie} points de vie pour {self.Nom}, donc il est encore en vie.")
            return True
        else:
            print(f"Il reste {self.Vie} points de vie pour {self.Nom}, donc il est mort.")
            return False

    def est_mort(self):
        if self.Vie <= 0:
            print(f"{self.Nom} est mort.")
            return True
        else:
            print(f"{self.Nom} est encore en vie.")
            return False

    def perd_vie(self, nb_points_de_vie_perdus):
        if nb_points_de_vie_perdus > 0:
            print(f"{self.Nom} perd {nb_points_de_vie_perdus} points de vie.")
            self.Vie -= nb_points_de_vie_perdus
        else:
            print(f"{self.Nom} encore en vie, nombre de points perdus {nb_points_de_vie_perdus}.")

    def gagne_vie(self, nb_points_de_vie_gagnes):
        if nb_points_de_vie_gagnes > 0:
            print(f"{self.Nom} gagne {nb_points_de_vie_gagnes} points de vie.")
            self.Vie += nb_points_de_vie_gagnes
        else:
            print("Le nombre de points de vie gagnés doit être supérieur à zéro.")

    def attaque(self, cible):
        if self.est_en_vie() and cible.est_en_vie():
            degat = self.Force * 0.6
            degats = round(degat)
            cible.perd_vie(degats)
            print(f"{self.Nom} attaque {cible.Nom} et lui inflige {degats} points de dégâts.")
        else:
            print("L'attaque ne peut pas être effectuée car l'attaquant ou la cible est morte.")

class MagicienHumain(Personnage):
    def __init__(self, nom, vie, force, endurance, rapidite, intelligence, race, points_de_magie):
        super().__init__(nom, vie, force, endurance, rapidite, intelligence)
        self.race = race
        self.points_de_magie = points_de_magie

    def faire_magie(self, cible, points_de_degats):
        if points_de_degats > 0:
            print(f"{self.Nom} lance un sort sur {cible.Nom} et lui inflige {points_de_degats} points de dégâts.")
            self.Vie -= points_de_degats
        elif points_de_degats < 0:
            soin = abs(points_de_degats)
            print(f"{self.Nom} lance un sort de soin sur {cible.Nom} et lui restaure {soin} points de vie.")
        else:
            print(f"{self.Nom} lance un sort sur {cible.Nom}, mais il n'y a aucun effet.")

Dicopersonnages = {}

def creationDicopersonnages(nom, vie, force, endurance, rapidite, intelligence):
    Dicopersonnages[nom] = Personnage(nom, vie, force, endurance, rapidite, intelligence)

def creationDicopersonnagesMagiciens(nom, vie, force, endurance, rapidite, intelligence, race, points_de_magie):
    Dicopersonnages[nom] = MagicienHumain(nom, vie, force, endurance, rapidite, intelligence, race, points_de_magie)

def GetObjetPersonnageByName(nom):
    monPersonnage = Dicopersonnages.get(nom, None)
    return monPersonnage

for i in range(1, 7):
    nom_personnage = f"Personnage{i}"
    creationDicopersonnagesMagiciens(nom_personnage, 10, 5, 4, 10, 5, "Humain", 14)

un_personnage = GetObjetPersonnageByName("Personnage1")
if un_personnage:
    print(f"Nom du personnage : {un_personnage.Nom}")
    un_personnage.afficher_info()

for i in range(1, 7):
    nom_personnage = f"Personnage{i}"
    creationDicopersonnagesMagiciens(nom_personnage, 15, 8, 3, 8, 9, "Hobbit", 9)

un_personnage = GetObjetPersonnageByName("Personnage2")
if un_personnage:
    print(f"Nom du personnage : {un_personnage.Nom}")
    un_personnage.afficher_info()

for i in range(1, 7):
    nom_personnage = f"Personnage{i}"
    creationDicopersonnagesMagiciens(nom_personnage, 0, 5, 7, 18, 5, "Naim", 6)

un_personnage = GetObjetPersonnageByName("Personnage3")
if un_personnage:
    print(f"Nom du personnage : {un_personnage.Nom}")
    un_personnage.afficher_info()

for i in range(1, 7):
    nom_personnage = f"Personnage{i}"
    creationDicopersonnagesMagiciens(nom_personnage, 17, 8, 4, 0, 8, "Orque", 12)

un_personnage = GetObjetPersonnageByName("Personnage4")
if un_personnage:
    print(f"Nom du personnage : {un_personnage.Nom}")
    un_personnage.afficher_info()




Pers0 = Personnage("Mokrane", 10, 11, 12, 8, 29)
Pers1 = Personnage("MAMER", 5, 9, 10, 4, 20)
Pers2 = Personnage("OLIVIE", 0, 5, 5, 1, 10)

Pers0.afficher_info()
Pers1.afficher_info()
Pers2.afficher_info()
print("***____________***")
print(Pers0.Nom)
Pers0.est_en_vie()
print("***____________***")
print(Pers1.Nom)
Pers1.est_en_vie()
print("***____________***")
print(Pers2.Nom)
Pers2.est_en_vie()
print("***____________***")
print(Pers0.Nom)
Pers0.est_mort()
print("***____________***")
print(Pers1.Nom)
Pers1.est_mort()
print("***____________***")
print(Pers2.Nom)
Pers2.est_mort()
print("***____________***")
Pers0.perd_vie(4)
Pers0.afficher_info()
print("***____________***")
Pers1.perd_vie(3)
Pers1.afficher_info()
print("***____________***")
Pers2.perd_vie(1)
Pers2.afficher_info()
print("***____________***")
Pers0.gagne_vie(5)
Pers0.afficher_info()
print("***____________***")
Pers1.gagne_vie(1)
Pers1.afficher_info()
print("***____________***")
Pers2.gagne_vie(2)
Pers2.afficher_info()
print("***____________***")
Pers0.attaque(Pers1)
Pers1.afficher_info()
Pers1.est_en_vie()
print("***____________***")
Pers0.attaque(Pers2)
Pers2.afficher_info()
Pers2.est_en_vie()
print("***____________***")
Pers0.attaque(un_personnage)