from labyrinthe_creation import Labyrinthe
import pygame

class Personnage:
    def __init__(self,window_surface,type): #type = 1 :perso de gauche         type = 2 : perso de droite
        if type == 1:
            self.speed = 15 # vitesse de déplacemant
            self.positionX = 15 # + 6 pour étre au centre des case comme le sprit fait de 5 par 5 et que les case font du 15 par 15
            self.positionY = 30*15
            self.etat = True # True = matérialiser, donc sensible au colision | False = dématérialiser, donc insensible au colision
            self.typee = 1
            self.image= pygame.image.load("image/perso1.png")
            self.image.convert_alpha()
            window_surface.blit(self.image,(self.positionX,self.positionY))
        if type == 2:
            self.speed = 15 # vitesse de déplacemant
            self.positionX = 505
            self.positionY = 30*15
            self.etat = False # True = matérialiser, donc sensible au colision | False = dématérialiser, donc insensible au colision
            self.typee = 2
            self.image= pygame.image.load("image/perso2.png")
            self.image.convert_alpha()
            window_surface.blit(self.image,(self.positionX,self.positionY))
    def affichage(self,window_surface):
        window_surface.blit(self.image,(self.positionX,self.positionY))
    def Xposition(self):
        return self.positionX
    def Yposition(self):
        return self.positionY
    ##
    def switch(self):
        if self.etat == True:
            self.etat = False
        else:
            self.etat = True
    ##
    # perso 1, X -15 Y-15
    # perso 2, X -505 Y - 15
    ##
    def peut_moveN(self,laby):
        if self.etat == False:
            return True
        else:
            if self.typee == 1:
                i = (self.positionX - 15) // 15
                j = (self.positionY -15) // 15
                if laby.laby[i][j].murN == 0 or laby.laby[i][j].murN == 2:
                    return True
                else:
                    return False
            else :
                i = (self.positionX - 505) // 15
                j = (self.positionY -15) // 15
                if laby.laby[i][j].murN == 0 or laby.laby[i][j].murN == 2:
                    return True
                else:
                    return False
    def peut_moveS(self,laby):
        if self.etat == False:
            return True
        else:
            if self.typee == 1:
                i = (self.positionX - 15) // 15
                j = (self.positionY -15) // 15
                if laby.laby[i][j].murS == 0 or laby.laby[i][j].murS == 2:
                    return True
                else:
                    return False
            else :
                i = (self.positionX - 505) // 15
                j = (self.positionY -15) // 15
                if laby.laby[i][j].murS == 0 or laby.laby[i][j].murS == 2:
                    return True
                else:
                    return False
    def peut_moveE(self,laby):
        if self.etat == False:
            return True
        else:
            if self.typee == 1:
                i = (self.positionX - 15) // 15
                j = (self.positionY -15) // 15
                if laby.laby[i][j].murE == 0 or laby.laby[i][j].murE == 2:
                    return True
                else:
                    return False
            else :
                i = (self.positionX - 505) // 15
                j = (self.positionY -15) // 15
                if laby.laby[i][j].murE == 0 or laby.laby[i][j].murE == 2:
                    return True
                else:
                    return False
    def peut_moveW(self,laby):
        if self.etat == False:
            return True
        else:
            if self.typee == 1:
                i = (self.positionX - 15) // 15
                j = (self.positionY -15) // 15
                if laby.laby[i][j].murW == 0 or laby.laby[i][j].murW == 2:
                    return True
                else:
                    return False
            else :
                i = (self.positionX - 505) // 15
                j = (self.positionY -15) // 15
                if laby.laby[i][j].murW  == 0 or laby.laby[i][j].murW == 2:
                    return True
                else:
                    return False
    ##
    def moveN(self,laby):
        self.positionY -= self.speed

    def moveS(self,laby):
        self.positionY += self.speed

    def moveW(self,laby):
        self.positionX -= self.speed

    def moveE(self,laby):
        self.positionX += self.speed

    ##



