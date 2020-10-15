# les conditions permettent de verifier une comparaison
# le resultat d'une comparaison est soit vrai, soit faut
# si le resultat est vrai alors, on execute le code de la condition
# il existe 3 conditions possible :
# if = si ...
# elif = sinon si ...
# else = sinon (par defaut)

# les different operateurs de comparaison sont :
# > strictement plus grand
# < strictement plus petit
# == egale
# >= plus grand ou egale
# <= plus petit ou egale
# != different, pas egale



chiffre = 10

if chiffre % 2 == 0: # si le reste de la division est egale a 0
    print("chiffre pair")
else:
    print("chiffre impair")

if chiffre > 10:
    print("plus grand que 10")
elif chiffre < 10:
    print("plus petit que 10")
else:
    print("est egale a 10")

text = "arbre"
lettre = "e"

if lettre in text:
    print(lettre,"est dans",text)
else:
    print(lettre,"n'est pas dans",text)
    

