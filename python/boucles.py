# En python, il existe 2 types de boucles
# while = tant que ...
# for = pour chaque ... 
# le resultat de la condition d'une boucle est soit:
# True (vrai)
# False (faux)

nombre = 10
flag = True

while nombre >= 0:
    print(nombre)
    nombre = nombre -1

print("--------------------")

while flag == True:
    print("ok")
    flag = False

print("--------------------")

for lettre in "maison":
    print(lettre)

print("--------------------")

phrase ="bientot la pause"
for lettre in phrase: # pour chaque lettre dans la phrase :
    if lettre in "aeiouy": # si la lettre est dans "aeiouy"
        print(lettre)   # on affiche la lettre

