#1 liste de mots **OK**
#2 choix aleatoire parmis les mots **OK**
#3 demander une lettre **OK**
#4 joueur donne une lettre **OK**
#5 si juste, ecrire lettre sinon retire une vie **OK**
    # si on a deja donne la lettre
    # sinon si la lettre est dans le mots a trouve (donc c'est juste)
    # sinon la lettre n'est pas dans le mots
    # dans les cas 2 et 3 on enregistre la lettre donne
#6 on affiche le mots masque **OK**
    # pour chaque lettre dans le mots a trouver, 
    # si la lettre a ete donne, on ajoute la lettre au mots masque
    # sinon on ajoute une etoile au mots masque
    # exemple : t**t pour le mots test
#7 repete les etapes 3->6 jusqu'a avoir trouve ou perdu

import random

liste_mots = [
    "armoire",
    "boucle",
    "couteau",
    "fichier",
    "journal",
    "montagne"
]

mots_a_trouver = random.choice(liste_mots)
nb_chances = 8
mots = ""
lettres_donnees = []
trouver= False

while trouver == False and nb_chances > 0 :
    print("taper une lettre")
    lettre = input(">> ")

    #si on a deja donne la lettre
    #sinon si la lettre est dans le mots a trouve (donc c'est juste)
    #sinon la lettre n'est pas dans le mots
    # dans les cas 2 et 3 on enregistre la lettre donne

    if lettre in lettres_donnees:
        print("la lettre", lettre,"a deja ete donnee")
    elif lettre in mots_a_trouver:
        print("c'est bon")
        lettres_donnees.append(lettre)
    else:
        print("pas bon")
        nb_chances = nb_chances-1

    # pour chaque lettre dans le mots a trouver, 
    # si la lettre a ete donne, on ajoute la lettre au mots masque
    # sinon on ajoute une etoile au mots masque
    # exemple : t**t pour le mots test
    mots_masque =""
    for lettre2 in mots_a_trouver:
        if lettre2 in lettres_donnees:
            mots_masque = mots_masque + lettre2
        else:
            mots_masque = mots_masque + "*"
    
    if mots_masque == mots_a_trouver :
        trouver = True
        print("Bravo, tu as trouvé le mots :", mots_a_trouver)
        print("il te restait",nb_chances,"chances")
    else:
        print(mots_masque)
        print("il te reste",nb_chances,"chances")




#print("mots masque =", mots_masque)
#print("chances =", nb_chances)
#print("lettres donnees =",lettres_donnees)




