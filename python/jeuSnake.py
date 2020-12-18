import pygame
import snake
import time
import random

pygame.init()
#On cree une variable pour eviter que notre jeu soit trop rapide.
#la vitesse de rafraichessement sera regle plus tard dans le code
clock = pygame.time.Clock()

score = 0

#variables utilisees pour la taille de l'ecran
ecranL = 400
ecranH = 300

#couleurs predefinies au cas ou on veut changer
rouge= (255,0,0)
vert= (0,255,0)
bleu= (0,0,255)
blanc= (255,255,255)
noir= (0,0,0)

#on genere un chiffre aleatoire qu'on divise par 10, puis on l'arrondit et enfin, on le remet sur "100"
#ex : 299 / 10 >>> 29.9 arrondi a 29 >>> 29 * 100 >>> 290
foodX= round(random.randrange(0,ecranL-10) / 10) * 10
foodY= round(random.randrange(0,ecranH-10) / 10) * 10

#on defini la taille de l'ecran
ecran = pygame.display.set_mode((ecranL,ecranH))

pygame.display.set_caption("Snake v0.1") #titre de la fenetre

gameOver = False
joueur = snake.Player("Toto",[ecranL,ecranH])

font_style = pygame.font.SysFont(None,50)

def message(msg, couleur):
    messageTemp = font_style.render(msg, True, couleur)
    ecran.blit(messageTemp, [ecranL/3,ecranH/3])


while not gameOver :
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameOver = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                joueur.haut()
            elif event.key == pygame.K_DOWN:
                joueur.bas()
            elif event.key == pygame.K_LEFT:
                joueur.gauche()
            elif event.key == pygame.K_RIGHT:
                joueur.droite()
    
    #detect si on sort de l'ecran
    if joueur.x >= ecranL or joueur.x < 0 or joueur.y >= ecranH or joueur.y < 0 :
        gameOver = True
    
    #detect si on mange food
    if joueur.x == foodX and joueur.y == foodY:
        print("miam")
        joueur.longueur += 1
        score += 100
        print(joueur.longueur)
        print(score)
        foodX= round(random.randrange(0,ecranL-10) / 10) * 10
        foodY= round(random.randrange(0,ecranH-10) / 10) * 10


    # Ici, on met a jour les variable.
    # On le fait ici plutot que durant la detection de l'evenement (ex K_UP)
    # pour que le serpent avance meme si on appuis pas sur une touche
    joueur.x += joueur.changeX
    joueur.y += joueur.changeY

    ecran.fill(blanc)
    tete=[]
    tete.append(joueur.x) # position[0]
    tete.append(joueur.y) # position[1]
    joueur.listeSnake.append(tete)
    
    if len(joueur.listeSnake) > joueur.longueur :
        del joueur.listeSnake[0]

    # on verifie si un des elements du serpent posede la meme position que la tete
    # si c'est le cas, c'est game over 
    for elementSerpent in  joueur.listeSnake[:-1]:
        if elementSerpent == tete:
            gameOver= True


    for position in joueur.listeSnake:
        pygame.draw.rect(ecran, joueur.colorRed, [position[0],position[1],joueur.taille,joueur.taille], border_radius=2 )

    #on dessine la nouriture    
    pygame.draw.rect(ecran,bleu,[foodX,foodY,10,10])
    pygame.display.update()

    #Ajout temps de rafraichissement qui defini la vitesse du jeu
    clock.tick(10)



message("Game Over", rouge)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
