import pygame
from pygame.locals import *
from random import randint, choice
from grosse_boule_bien_rouge_donc_bien_chaude import Boule
from pile import Pile

class Case:
    def __init__(self):     #True = 0(pas de mure)        False = 1(mure entier)    2= mure casser(vide)         3=mure rajouté
        self.murN = 1
        self.murW = 1
        self.murS = 1
        self.murE = 1
        self.vue = False
        self.boule = False
        self.nb = None
class Mure:
    def __init__(self,i,j): # création des différent murs afin de les faire apparaitre au bonne endroit.
        self.murcommun1N = pygame.Rect(i-2+10,j-2+10,19,4)
        self.murcommun1S = pygame.Rect(i-2+10,j+13+10,19,4)
        self.murcommun1W = pygame.Rect(i-2+10,j-2+10, 4, 19)
        self.murcommun1E = pygame.Rect(i+13+10,j-2+10, 4, 19)
        self.mur1N = pygame.Rect(i+10,j+10,15,2)
        self.mur1S = pygame.Rect(i+10,j+13+10, 15,2)
        self.mur1W = pygame.Rect(i+10,j+10,2,15)
        self.mur1E = pygame.Rect(i+13+10,j+10,2,15)
        ###
        # a modifier pour permetre adaptabilité
        self.murcommun2N = pygame.Rect(i-2+500,j-2+10,19,4)
        self.murcommun2S = pygame.Rect(i-2+500,j+13+10,19,4)
        self.murcommun2W = pygame.Rect(i-2+500,j-2+10, 4, 19)
        self.murcommun2E = pygame.Rect(i+13+500,j-2+10, 4, 19)
        self.mur2N = pygame.Rect(i+500,j+10,15,2)
        self.mur2S = pygame.Rect(i+500,j+13+10, 15,2)
        self.mur2W = pygame.Rect(i+500,j+10,2,15)
        self.mur2E = pygame.Rect(i+13+500,j+10,2,15)
    def colision(self,personage):
        pass


class Labyrinthe:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.laby = [[Case() for j in range(hauteur)] for i in range(largeur)]

    def __directions_possibles(self,i,j):
        directions = []
        if j < self.hauteur-1 and not self.laby[i][j+1].vue:
            directions.append('S')
        if i > 0 and not self.laby[i-1][j].vue:
            directions.append('W')
        if j > 0 and not self.laby[i][j-1].vue:
            directions.append('N')
        if i < self.largeur-1 and not self.laby[i+1][j].vue:
            directions.append('E')
        return directions

    def __abattre_mur(self,i,j,dir,pile):
        if dir == 'S':
            self.laby[i][j].murS = 0
            self.laby[i][j+1].murN = 0
            self.laby[i][j+1].vue = True
            pile.empiler((i, j+1))
        elif dir == 'W':
            self.laby[i][j].murW = 0
            self.laby[i-1][j].murE = 0
            self.laby[i-1][j].vue = True
            pile.empiler((i-1, j))
        elif dir == 'N':
            self.laby[i][j].murN = 0
            self.laby[i][j-1].murS = 0
            self.laby[i][j-1].vue = True
            pile.empiler((i, j-1))
        else:
            self.laby[i][j].murE = 0
            self.laby[i+1][j].murW = 0
            self.laby[i+1][j].vue = True
            pile.empiler((i+1, j))
    def generer(self):
        pile = Pile()
        i, j = randint(0,self.largeur-1), randint(0,self.hauteur-1)
        pile.empiler((i, j))
        self.laby[i][j].vue = True
        while not pile.est_vide():
            (i, j) = pile.depiler()
            directions = self.__directions_possibles(i,j)
            if len(directions) > 1:
                pile.empiler((i, j))
            if len(directions) > 0:
                dir = choice(directions)
                self.__abattre_mur(i,j,dir,pile)

    def contour(self):
        for i in range(self.largeur):
            self.laby[0][i].murW = 1
            self.laby[self.largeur-1][i].murE = 1
        for j in range(self.hauteur):
            self.laby[j][0].murN = 1
            self.laby[j][self.hauteur-1].murS = 1

    def casse_mure(self,nb,):
        for y in range(nb):
            i, j = randint(0,self.largeur-1), randint(0,self.hauteur-1)
            f, e = randint(0,self.largeur-1), randint(0,self.hauteur-1)
            tmp = randint(0,3) #choisire le coté
            if tmp == 0 :
                if self.laby[i][j].murW == 1:
                    self.laby[i][j].murW = 2
                if self.laby[i-1][j].murE == 1:
                    self.laby[i-1][j].murE = 2
            if tmp == 1 :
                if self.laby[f][e].murS == 1:
                    self.laby[f][e].murS = 2
                if e+1 <= self.hauteur-1 :
                    if self.laby[f][e+1].murN == 1:
                        self.laby[f][e+1].murN = 0
            if tmp == 2 :
                if self.laby[i][j].murE == 1:
                    self.laby[i][j].murE = 2
                if i+1 <= self.largeur-1 :
                    if self.laby[i+1][j].murW == 1:
                        self.laby[i+1][j].murW = 2
            if tmp == 3 :
                if self.laby[f][e].murN == 1:
                    self.laby[f][e].murN = 2
                if self.laby[f][e-1].murS == 1:
                    self.laby[f][e-1].murS = 2

    def pop_mure(self,nb):
        for y in range(nb):
            i, j = randint(0,self.largeur-1), randint(0,self.hauteur-1)
            f, e = randint(0,self.largeur-1), randint(0,self.hauteur-1)
            tmp = randint(0,3) #choisire le coté
            if tmp == 0 :
                if self.laby[i][j].murW == 0:
                    self.laby[i][j].murW = 3
                if self.laby[i-1][j].murE == 0:
                    self.laby[i-1][j].murE = 3
            if tmp == 1 :
                if self.laby[f][e].murS == 0:
                    self.laby[f][e].murS = 3
                if e+1 <= self.hauteur-1 :
                    if self.laby[f][e+1].murN == 0:
                        self.laby[f][e+1].murN = 3
            if tmp == 2 :
                if self.laby[i][j].murE == 0:
                    self.laby[i][j].murE = 3
                if i+1 <= self.largeur-1 :
                    if self.laby[i+1][j].murW == 0:
                        self.laby[i+1][j].murW = 3
            if tmp == 3 :
                if self.laby[f][e].murN == 0:
                    self.laby[f][e].murN = 3
                if self.laby[f][e-1].murS == 0:
                    self.laby[f][e-1].murS = 3

    def random(self,nb):
        self.casse_mure(nb)
        self.pop_mure(nb)
    def random2(self,nb1,nb2):
        self.casse_mure(nb1)
        self.pop_mure(nb2)

    def mur0(self,window_surface,nb):
        pass
    def mur1(self,window_surface,nb):
        if nb == 1 :
            couleur_mur1 = (10,10,10)
            for i in range(self.largeur):
                for j in range(self.hauteur):
                    mure_laby = Mure(i*15,j*15)
                    if i == self.largeur-1:
                        if self.laby[i][j].murE == 1 :
                            pygame.draw.rect(window_surface,couleur_mur1,mure_laby.murcommun1E)

                    if j == self.hauteur-1:
                        if self.laby[i][j].murS == 1 :
                            pygame.draw.rect(window_surface,couleur_mur1,mure_laby.murcommun1S)

                    if self.laby[i][j].murN == 1 :
                        if self.laby[i][j-1].murS==1:
                            pygame.draw.rect(window_surface,couleur_mur1,mure_laby.murcommun1N)

                    if self.laby[i][j].murW == 1 :
                        if self.laby[i-1][j].murE==1:
                            pygame.draw.rect(window_surface,couleur_mur1,mure_laby.murcommun1W)
        if nb == 2:
            couleur_mur1 = (10,10,10)
            for i in range(self.largeur):
                for j in range(self.hauteur):
                    mure_laby = Mure(i*15,j*15)
                    if i == self.largeur-1:
                        if self.laby[i][j].murE == 1 :
                            pygame.draw.rect(window_surface,couleur_mur1,mure_laby.murcommun2E)

                    if j == self.hauteur-1:
                        if self.laby[i][j].murS == 1 :
                            pygame.draw.rect(window_surface,couleur_mur1,mure_laby.murcommun2S)

                    if self.laby[i][j].murN == 1 :
                        if self.laby[i][j-1].murS==1:
                            pygame.draw.rect(window_surface,couleur_mur1,mure_laby.murcommun2N)

                    if self.laby[i][j].murW == 1 :
                        if self.laby[i-1][j].murE==1:
                            pygame.draw.rect(window_surface,couleur_mur1,mure_laby.murcommun2W)

    def mur2(self,window_surface,nb):
        pass
    def mur3(self,window_surface,nb):
        if nb == 1:
            couleur_mur3 = (255,0,0)
            for i in range(self.largeur):
                for j in range(self.hauteur):
                    mure_laby = Mure(i*15,j*15)
                    if self.laby[i][j].murN == 3 :
                        if self.laby[i][j-1].murS==3:
                            pygame.draw.rect(window_surface,couleur_mur3,mure_laby.murcommun1N)
                    if self.laby[i][j].murW == 3 :
                        if self.laby[i-1][j].murE==3:
                            pygame.draw.rect(window_surface,couleur_mur3,mure_laby.murcommun1W)
        couleur_mur3 = (255,0,0)
        if nb == 2:
            couleur_mur3 = (50,50,255)
            for i in range(self.largeur):
                for j in range(self.hauteur):
                    mure_laby = Mure(i*15,j*15)
                    if self.laby[i][j].murN == 3 :
                        if self.laby[i][j-1].murS==3:
                            pygame.draw.rect(window_surface,couleur_mur3,mure_laby.murcommun2N)
                    if self.laby[i][j].murW == 3 :
                        if self.laby[i-1][j].murE==3:
                            pygame.draw.rect(window_surface,couleur_mur3,mure_laby.murcommun2W)
    ##
    def font_case1(self,window_surface):
        self.image= pygame.image.load("image/1.jpg")
        self.image.convert_alpha()
        for i in range(self.largeur):
            for j in range(self.hauteur):
                window_surface.blit(self.image,(i*15+10,j*15+10))
    def font_case2(self,window_surface):
        self.image= pygame.image.load("image/2.jpg")
        self.image.convert_alpha()
        for i in range(self.largeur):
            for j in range(self.hauteur):
                window_surface.blit(self.image,(i*15+500,j*15+10))
    ##
    def boule_true(self,i,j,nb):
        self.laby[i][j].boule = True
        self.laby[i][j].nb = nb
    def boule_false(self,i,j):
        self.laby[i][j].boule = False
    def return_boule(self,i,j):
        return self.laby[i][j].boule
    def return_nb(self,i,j):
        return self.laby[i][j].nb
    ##
    def afficher1(self,window_surface):
        violet = (255,56,211)
        couleur_mur1 = (10,10,10)
        couleur_mur3 = (255,0,0)
        couleur_mur2 = (200,150,0)

        #emplacement_laby = pygame.Rect(10,10,self.largeur*15,self.hauteur*15)
        #pygame.draw.rect(window_surface,violet,emplacement_laby)
        self.font_case1(window_surface)
        self.mur3(window_surface,1)
        self.mur1(window_surface,1)

##################################################################################################################################
    def afficher2(self,window_surface):
        bleu_ciel = (25,255,211)
        couleur_mur1 = (10,10,10)
        couleur_mur3 = (50,50,255)
        couleur_mur2 = (200,200,255)

        #emplacement_laby = pygame.Rect(500,10,self.largeur*15,self.hauteur*15)
        #pygame.draw.rect(window_surface,bleu_ciel,emplacement_laby)
        self.font_case2(window_surface)
        self.mur3(window_surface,2)
        self.mur1(window_surface,2)
###################

    def copy_laby(self,list):
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.laby[i][j].murN = list.laby[i][j].murN
                self.laby[i][j].murS = list.laby[i][j].murS
                self.laby[i][j].murW = list.laby[i][j].murW
                self.laby[i][j].murE = list.laby[i][j].murE




