import random

class Joueur:
    nom =""
    age = 0
    vie = 20


    def __init__(self, nom, age): #constructeur
        self.nom = nom
        self.age = age

    def presentation(self):
        print("Bonjour, je m'appelle", self.nom, "j'ai", self.age,"ans")

    def tape(self, Joueur):
        degats = random.randint(1,3)

        print(self.nom, "tape", Joueur.nom, "il lui fait", degats, "de degats")
        Joueur.vie = Joueur.vie - degats
        print("Il reste a", Joueur.nom, Joueur.vie,"points de vie")
    
    def mort(self):
        print(self.nom,": Arrg, je suis mort")

joueur1 = Joueur("Abou", 18)
joueur2 = Joueur("Simon", 34)

while joueur1.vie > 0 and joueur2.vie > 0:
    joueur1.tape(joueur2)
    joueur2.tape(joueur1)

if joueur1.vie <= 0 and joueur2.vie <= 0:
    print("match nul")
elif joueur1.vie > 0:
    joueur2.mort()
    print(joueur1.nom, "gagne")
else:
    joueur1.mort()
    print(joueur2.nom, "gagne")








