############
#Principal
############
from moviepy.editor import *
from game import Jeu
import pygame


pygame.display.set_caption('Hello World!')

clip = VideoFileClip('video/intro.mp4')
clip.preview()
pygame.quit()



jeu = Jeu()
jeu.game()


# ne pas oublier le "pip install moviepy"

### Commende du jeu
"""
ZQSD et/ou flèche directionnel : déplacer le personnage
espace : changer de labyrinthe
E et/ou 0(celui du paver numérique) : intéragire (prendre les boule)
echape : enlever ou re metre le "décore" du premier plan qui peut géné la vision des fois
"""

### but du jeu
"""
ramasser toute les boule (10) afin de débliquer l'écrant de victoire
"""

### complexité temporelle
"""
il y a pas mal de petit calcul qui sont inutil (enfin qui pourais étre remplacer par des valeurs, cec qui ferais des opération en moins)
la raison de leur présence est que lors du dévelopement, c'étais plus simple pour comprendre ce que l'on fessais, je n'est juste pas pris le temps de les remplacer parce qu'il est tard, ou tôt, ça dépant dans quelle sense on aborde le sujet. (5h17 a l'heurs au j'écris cette phrase.)
"""

### L'heurs a la quelle ce jeu a étais fini ?
"""
5h04 du matin, et non je ne me suis pas levais tôt (belle et bien une casi nuit blanche xD)
"""