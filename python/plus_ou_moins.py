# on importe une librairie pour choisir un nombre aleatoire
import random

# on cree une variable nombre_cache
# on y stock un nombre aleatoire entre 0 et 100
# on fait appel a la fonction randint qui se trouve dans random
nombre_cache = random.randint(0,100)
trouver = False

while trouver == False:
    print("Tape une nombre entre 0 et 100")
    entree_joueur = int( input(">>") )

    if entree_joueur < nombre_cache :
        print("ton nombre est trop petit")
    elif entree_joueur > nombre_cache:
        print("ton nombre est trop grand")
    else :
        print("bravo !")
        trouver= True


