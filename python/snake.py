class Player:
    prenom="" 
    colorBlue =(0,0,255) # RGB  Red / Green / Blue
    colorRed = (255,0,0)
    #position du serpent
    x =0
    y =0
    #changement a faire sur la position du sperpent
    changeX= 0
    changeY= 0
    taille = 10 #taille du carre des anneaux du serpent
    longueur= 1 #nb de carre pour le serpent
    listeSnake=[] #liste qui comprend la position de chaque anneau
    speed = 10

    #pour cree notre serpent, il lui faut un nom et une position de depart X et Y
    def __init__(self, prenom,position):
        self.prenom = prenom
        self.x =position[0]/2
        self.y = position[1]/2

    #On enregistrement le changement a faire en fonction de la direction qu'on prend
    def haut(self) :
        self.changeY -= self.speed
        self.changeX = 0
    def bas(self) :
        self.changeY += self.speed
        self.changeX = 0
    def gauche(self) :
        self.changeX -= self.speed
        self.changeY=0
    def droite(self) :
        self.changeX += self.speed
        self.changeY=0
    