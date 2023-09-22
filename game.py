from labyrinthe_creation import Labyrinthe
from personnage import Personnage
from grosse_boule_bien_rouge_donc_bien_chaude import Boule
from random import randint, choice
import pygame



class Jeu:
    def __init__(self):
        pygame.init()


        resolution_fenetre = (960, 799)
        #courleur_python = (R, G, B) (chaque valeur va de 0 a 255)(R = rouge, G = vert, B = bleu) (0,0,0) = noir, (255,255,255) =blanc
        self.blue_color = (89,152,255)
        self.blanc = (255,255,255)
        self.rouge =(255,50,100)
        self.noire =(0,0,0)
        self.violet = (255,56,211)
        self.jaune = (255,255,0)
        pygame.display.set_caption("Switch the lab")

        self.window_surface = pygame.display.set_mode(resolution_fenetre,pygame.RESIZABLE|pygame.DOUBLEBUF|pygame.HWSURFACE)
        self.window_surface.fill(self.blue_color)
        ##
        self.arial_font = pygame.font.SysFont("arial", 20, True, False)
        self.arial_font2 = pygame.font.SysFont("arial", 35, True, True)

        ###
        self.reki= pygame.image.load("image/B.png")
        self.reki.convert()

        self.font = pygame.image.load("image/A.png")
        self.font.convert_alpha()
        ###
        pygame.mixer.music.load('musique/freeze-rael-version-8bit.mp3')
        pygame.mixer.music.play(-1)
        ###
        self.score1= 0
        self.score2= 0
        self.laby_main = True
        self.decord = True

        self.laby_1=Labyrinthe(30,30)
        self.laby_1.generer()
        self.laby_2 = Labyrinthe(30,30)
        self.laby_2.copy_laby(self.laby_1)
        self.laby_2.random(100)
        self.laby_1.random(100)

        self.laby_1.contour()
        self.laby_2.contour()
        self.perso1 = Personnage(self.window_surface,1)
        self.perso2 = Personnage(self.window_surface,2)
        self.pop_boule()
        self.incruste_boule()
        ###
    def game(self):
        launched = True
        not_end = True
        while not_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    not_end = False
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP) or (event.key == pygame.K_z):
                        self.allezN()
                    if (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
                        self.allezS()
                    if (event.key == pygame.K_LEFT) or (event.key == pygame.K_q):
                        self.allezW()
                    if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                        self.allezE()
                    if event.key == pygame.K_SPACE :
                        self.change_type()
                    if (event.key == pygame.K_KP0) or (event.key == pygame.K_e):
                        self.interactionE()
                    #if event.key == pygame.K_v :
                    #    self.technique_secrette_du_dev()
                    if event.key == pygame.K_ESCAPE :
                        if self.decord == True:
                            self.decord = False
                        else:
                            self.decord = True

            if launched == True :
                self.affichage()
            else:
                self.affichage_victoire()
            if self.score1 == 5 and self.score2 == 5:
                launched = False
            pygame.display.flip()




        pygame.quit()
    def technique_secrette_du_dev(self): #victoir instantané
        self.score1 = 5
        self.score2 = 5
    def affichage_victoire(self):
        self.fin= pygame.image.load("image/victoire1.jpg")
        self.fin.convert()
        self.window_surface.blit(self.fin,(0,0))
    def affichage(self):
            self.window_surface.fill(self.blue_color)
            self.window_surface.blit(self.reki,(0,0))
            self.laby_1.afficher1(self.window_surface)
            self.laby_2.afficher2(self.window_surface)
            #self.laby_1.font_case1(self.window_surface)
            self.afficher_boule()
            self.perso1.affichage(self.window_surface)
            self.perso2.affichage(self.window_surface)
            self.texte_etat() #le cadre jaune qui nous informe de quelle coté on doit jouer
            if self.decord == True:
                self.window_surface.blit(self.font,(0,0))
            self.texte_commande()
            self.texte_score()
    def interactionE(self):
        if self.laby_main == True:
            if self.laby_1.return_boule((self.perso1.Xposition()-15)//15,(self.perso1.Yposition()-15)//15) == True:
                self.laby_1.boule_false((self.perso1.Xposition()-15)//15,(self.perso1.Yposition()-15)//15)
                if self.laby_1.return_nb((self.perso1.Xposition()-15)//15,(self.perso1.Yposition()-15)//15) == 1:
                    self.boule1.etat_false()
                    self.score1 +=1
                elif self.laby_1.return_nb((self.perso1.Xposition()-15)//15,(self.perso1.Yposition()-15)//15) == 2:
                    self.boule2.etat_false()
                    self.score1 +=1
                elif self.laby_1.return_nb((self.perso1.Xposition()-15)//15,(self.perso1.Yposition()-15)//15) == 3:
                    self.boule3.etat_false()
                    self.score1 +=1
                elif self.laby_1.return_nb((self.perso1.Xposition()-15)//15,(self.perso1.Yposition()-15)//15) == 4:
                    self.boule4.etat_false()
                    self.score1 +=1
                elif self.laby_1.return_nb((self.perso1.Xposition()-15)//15,(self.perso1.Yposition()-15)//15) == 5:
                    self.boule5.etat_false()
                    self.score1 +=1
        else:
            if self.laby_2.return_boule((self.perso2.Xposition()-505)//15,(self.perso2.Yposition()-15)//15) == True:
                self.laby_2.boule_false((self.perso2.Xposition()-505)//15,(self.perso2.Yposition()-15)//15)
                if self.laby_2.return_nb((self.perso2.Xposition()-505)//15,(self.perso2.Yposition()-15)//15) == 6:
                    self.boule6.etat_false()
                    self.score2 += 1
                elif self.laby_2.return_nb((self.perso2.Xposition()-505)//15,(self.perso2.Yposition()-15)//15) == 7:
                    self.boule7.etat_false()
                    self.score2 += 1
                elif self.laby_2.return_nb((self.perso2.Xposition()-505)//15,(self.perso2.Yposition()-15)//15) == 8:
                    self.boule8.etat_false()
                    self.score2 += 1
                elif self.laby_2.return_nb((self.perso2.Xposition()-505)//15,(self.perso2.Yposition()-15)//15) == 9:
                    self.boule9.etat_false()
                    self.score2 += 1
                elif self.laby_2.return_nb((self.perso2.Xposition()-505)//15,(self.perso2.Yposition()-15)//15) == 10:
                    self.boule10.etat_false()
                    self.score2 += 1


    def change_type(self):
        self.perso1.switch()
        self.perso2.switch()
        if self.laby_main == True:
            self.laby_main = False
        else:
            self.laby_main = True
    def allezN(self):
        if self.perso1.peut_moveN(self.laby_1) == True and self.perso2.peut_moveN(self.laby_2) == True :
            self.perso1.moveN(self.laby_1)
            self.perso2.moveN(self.laby_2)
    def allezS(self):
        if self.perso1.peut_moveS(self.laby_1) == True and self.perso2.peut_moveS(self.laby_2) == True :
            self.perso1.moveS(self.laby_1)
            self.perso2.moveS(self.laby_2)
    def allezE(self):
        if self.perso1.peut_moveE(self.laby_1) == True and self.perso2.peut_moveE(self.laby_2) == True :
            self.perso1.moveE(self.laby_1)
            self.perso2.moveE(self.laby_2)
    def allezW(self):
        if self.perso1.peut_moveW(self.laby_1) == True and self.perso2.peut_moveW(self.laby_2) == True :
            self.perso1.moveW(self.laby_1)
            self.perso2.moveW(self.laby_2)
    ######################################
    def pop_boule(self):
        i, j = randint(0,29), randint(0,29)
        f, e = randint(0,29), randint(0,29)
        a, z = randint(0,29), randint(0,29)
        r, t = randint(0,29), randint(0,29)
        y, u = randint(0,29), randint(0,29)
        o, p = randint(0,29), randint(0,29)
        q, s = randint(0,29), randint(0,29)
        d, g = randint(0,29), randint(0,29)
        h, k = randint(0,29), randint(0,29)
        l, m = randint(0,29), randint(0,29)
        #
        self.boule1 = Boule(self.window_surface,i,j,1,1)
        self.boule2 = Boule(self.window_surface,f,e,1,2)
        self.boule3 = Boule(self.window_surface,a,z,1,3)
        self.boule4 = Boule(self.window_surface,r,t,1,4)
        self.boule5 = Boule(self.window_surface,y,u,1,5)
        self.boule6 = Boule(self.window_surface,o,p,2,6)
        self.boule7 = Boule(self.window_surface,q,s,2,7)
        self.boule8 = Boule(self.window_surface,d,g,2,8)
        self.boule9 = Boule(self.window_surface,h,k,2,9)
        self.boule10 = Boule(self.window_surface,l,m,2,10)
        # les deux boule suivante sont celle qui serve a ilustrès le compteur.
        self.boule11 = Boule(self.window_surface,400,470,3,11)
        self.boule12 = Boule(self.window_surface,900,470,4,12)
        ##

    def afficher_boule(self):
        self.boule1.affichage(self.window_surface)
        self.boule2.affichage(self.window_surface)
        self.boule3.affichage(self.window_surface)
        self.boule4.affichage(self.window_surface)
        self.boule5.affichage(self.window_surface)
        self.boule6.affichage(self.window_surface)
        self.boule7.affichage(self.window_surface)
        self.boule8.affichage(self.window_surface)
        self.boule9.affichage(self.window_surface)
        self.boule10.affichage(self.window_surface)

        self.boule11.affichage(self.window_surface)
        self.boule12.affichage(self.window_surface)

    def incruste_boule(self):
        self.laby_1.boule_true(self.boule1.lab_positionX(),self.boule1.lab_positionY(),1)
        self.laby_1.boule_true(self.boule2.lab_positionX(),self.boule2.lab_positionY(),2)
        self.laby_1.boule_true(self.boule3.lab_positionX(),self.boule3.lab_positionY(),3)
        self.laby_1.boule_true(self.boule4.lab_positionX(),self.boule4.lab_positionY(),4)
        self.laby_1.boule_true(self.boule5.lab_positionX(),self.boule5.lab_positionY(),5)
        self.laby_2.boule_true(self.boule6.lab_positionX(),self.boule6.lab_positionY(),6)
        self.laby_2.boule_true(self.boule7.lab_positionX(),self.boule7.lab_positionY(),7)
        self.laby_2.boule_true(self.boule8.lab_positionX(),self.boule8.lab_positionY(),8)
        self.laby_2.boule_true(self.boule9.lab_positionX(),self.boule9.lab_positionY(),9)
        self.laby_2.boule_true(self.boule10.lab_positionX(),self.boule10.lab_positionY(),10)
    def texte_commande(self):
        #perso 1
        self.texte_de_position1  = self.arial_font.render(" perso 1 position X:",True, self.blanc)
        self.window_surface.blit(self.texte_de_position1, (5,10 + 30*15))
        self.texte_de_position2  = self.arial_font.render(" perso 1 position Y:",True, self.blanc)
        self.window_surface.blit(self.texte_de_position2, (5,30 + 30*15))

        self.texte_de_position3  = self.arial_font.render("{}".format(self.perso1.Yposition()),True, self.rouge)
        self.window_surface.blit(self.texte_de_position3, (200,30 + 30*15))
        self.texte_de_position4  = self.arial_font.render("{}".format(self.perso1.Xposition()),True, self.rouge)
        self.window_surface.blit(self.texte_de_position4, (200,10 + 30*15))

        #perso 2
        self.texte_de_position_1  = self.arial_font.render(" perso 2 position X:",True, self.blanc)
        self.window_surface.blit(self.texte_de_position_1, (500,10 + 30*15))
        self.texte_de_position_2  = self.arial_font.render(" perso 2 position Y:",True, self.blanc)
        self.window_surface.blit(self.texte_de_position_2, (500,30 + 30*15))

        self.texte_de_position_3  = self.arial_font.render("{}".format(self.perso2.Yposition()),True, self.rouge)
        self.window_surface.blit(self.texte_de_position_3, (700,30 + 30*15))
        self.texte_de_position_4  = self.arial_font.render("{}".format(self.perso2.Xposition()),True, self.rouge)
        self.window_surface.blit(self.texte_de_position_4, (700,10 + 30*15))

    def texte_etat(self):
        if self.laby_main == True :
            self.texte_de_position1  = self.arial_font2.render("←",True, self.jaune)
            self.window_surface.blit(self.texte_de_position1, (463,30))
            self.texte_de_position2  = self.arial_font2.render("←",True, self.rouge)
            self.window_surface.blit(self.texte_de_position2, (463,230))
            self.texte_de_position3  = self.arial_font2.render("←",True, self.jaune)
            self.window_surface.blit(self.texte_de_position3, (463,430))

            self.cadre = pygame.Rect(10,10,30*15,30*15)
            pygame.draw.rect(self.window_surface,self.jaune,self.cadre,4)
        else:
            self.texte_de_position1  = self.arial_font2.render("→",True, self.jaune)
            self.window_surface.blit(self.texte_de_position1, (463,30))
            self.texte_de_position2  = self.arial_font2.render("→",True, self.rouge)
            self.window_surface.blit(self.texte_de_position2, (463,230))
            self.texte_de_position3  = self.arial_font2.render("→",True, self.jaune)
            self.window_surface.blit(self.texte_de_position3, (463,430))

            self.cadre = pygame.Rect(500,10,30*15,30*15)
            pygame.draw.rect(self.window_surface,self.jaune,self.cadre,4)
    def texte_score(self):
        if self.score1 == 0:
            self.texte_score1  = self.arial_font.render("0/5",True, self.blanc)
            self.window_surface.blit(self.texte_score1, (410,462))
        elif self.score1 == 1:
            self.texte_score1  = self.arial_font.render("1/5",True, self.blanc)
            self.window_surface.blit(self.texte_score1, (410,462))
        elif self.score1 == 2:
            self.texte_score1  = self.arial_font.render("2/5",True, self.blanc)
            self.window_surface.blit(self.texte_score1, (410,462))
        elif self.score1 == 3:
            self.texte_score1  = self.arial_font.render("3/5",True, self.blanc)
            self.window_surface.blit(self.texte_score1, (410,462))
        elif self.score1 == 4:
            self.texte_score1  = self.arial_font.render("4/5",True, self.blanc)
            self.window_surface.blit(self.texte_score1, (410,462))
        elif self.score1 == 5:
            self.texte_score1  = self.arial_font.render("5/5",True, self.jaune)
            self.window_surface.blit(self.texte_score1, (410,462))
        ##
        if self.score2 == 0:
            self.texte_score2  = self.arial_font.render("0/5",True, self.blanc)
            self.window_surface.blit(self.texte_score2, (910,462))
        elif self.score2 == 1:
            self.texte_score2  = self.arial_font.render("1/5",True, self.blanc)
            self.window_surface.blit(self.texte_score2, (910,462))
        elif self.score2 == 2:
            self.texte_score2  = self.arial_font.render("2/5",True, self.blanc)
            self.window_surface.blit(self.texte_score2, (910,462))
        elif self.score2 == 3:
            self.texte_score2  = self.arial_font.render("3/5",True, self.blanc)
            self.window_surface.blit(self.texte_score2, (910,462))
        elif self.score2 == 4:
            self.texte_score2  = self.arial_font.render("4/5",True, self.blanc)
            self.window_surface.blit(self.texte_score2, (910,462))
        elif self.score2 == 5:
            self.texte_score2  = self.arial_font.render("5/5",True, self.jaune)
            self.window_surface.blit(self.texte_score2, (910,462))

