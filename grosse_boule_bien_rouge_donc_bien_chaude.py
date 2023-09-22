import pygame
#Moi Théotime BORDARIER KÖNIG refuse catégoriquement d'assumer le nom de ce fichier
class Boule:
    def __init__(self,window_surface,i,j,type,nb):
        self.etat = True # True = visible, False = cacher
        self.type = type
        nb = nb
        if self.type == 1 :
            self.positionX = i*15+12
            self.positionY = j*15+12
            self.image= pygame.image.load("image/grosse_boule_bien_bleu.png")
        elif self.type == 2 :
            self.positionX = i*15+504
            self.positionY = j*15+12
            self.image= pygame.image.load("image/grosse_boule_bien_rouge.png")
        elif self.type == 3 :
            self.positionX = i
            self.positionY = j
            self.image= pygame.image.load("image/grosse_boule_bien_bleu.png")
        elif self.type == 4 :
            self.positionX = i
            self.positionY = j
            self.image= pygame.image.load("image/grosse_boule_bien_rouge.png")
        self.image.convert_alpha()
        window_surface.blit(self.image,(self.positionX,self.positionY))


    def affichage(self,window_surface):
        if self.etat == True:
            window_surface.blit(self.image,(self.positionX,self.positionY))
    #def position_laby(self,laby):
    #    self.laby[i][j].boule = True
    def return_etat(self):
        return self.etat

    def etat_false(self):
        self.etat = False
    def return_type(self):
        return self.type
    def lab_positionX(self):
        if self.type == 1:
            return (self.positionX -12) //15
        else:
            return (self.positionX - 504) //15
    def lab_positionY(self):
        return (self.positionY - 12) //15