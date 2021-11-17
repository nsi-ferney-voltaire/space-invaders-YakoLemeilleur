import pygame
import random
        
class Joueur () : # classe pour créer le vaisseau du joueur
    def __init__(self):
        self.image = pygame.image.load ("vaisseau.png")
        self.position = 400
        self.direction = 0
        self.score = 0
        
    def setDirection(self, direction : str):
        if direction == "gauche":
            self.direction = "gauche"
        if direction == "droite":
            self.direction = "droite"
        
    def getPosition(self):
        return self.position
    
    def deplacer (self) :
        if self.direction =="gauche":
            self.position -=7
        if self.direction =="droite":
            self.position += 7
        self.position = min(max(self.position, 0), 737)
    
    def tirer(self):
       self.direction = 0
    
    def marquer():
        player.score += 1 
        

class Balle():
    def __init__(self, joueur):
        self.tireur = joueur
        self.depart = joueur.position 
        self.hauteur = 500
        self.image = pygame.image.load ("balle.png")
        self.etat = ' '
        self
    
    def bouger (self) :
        if self.etat =='tiree':
            self.hauteur -= 15
            if self.hauteur < 0 :
                self.depart = self.tireur.position
                self.hauteur = 500
                self.etat = 'chargee'
        if self.etat =='chargee':
            self.depart = self.tireur.position
            
    def toucher(self, ennemi) :
        if (ennemi.hauteur +  ) 
            return True
        return False
        

class Jeu():
    
    def __init__(self):
        self.nbEnnemis = random.randint(2,10)


class Ennemi():
    
    
    def __init__(self):
        self.depart = random.randint(0, 800)
        self.hauteur = 0
        self.type = random.randint(1, 2)
        self.vitesse = self.type *2
        self.image = pygame.image.load(f"invader{self.type}.png")
                
    def avancer(self):
        self.hauteur += self.vitesse 
        
    def disparaitre(self):
        self.hauteur += 1000
               
            
        
        