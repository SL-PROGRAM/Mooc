"""

Auteur: Simon LEYRAL
Date : Octobre 2017

Enoncé

ÉNONCÉ DU PROJET VASARELY

Description globale du projet

Il vous est demandé de réaliser un programme en Python produisant des tableaux d’art optique
avec différentes couleurs et déformations

Ces tableaux représentent des pavages hexagonaux, vus d’en haut, formés avec des losanges de couleurs différentes,
déformés par une boule. Votre programme utilisera le module turtle, présenté au module 2 de ce cours,
pour peindre vos tableaux.

"""


import turtle
import math
import deformation
"""
importation des bibliotheques deformation, turtle et Math necessaire au bon fonctionnement du script

"""


def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    """
    La fonction pavage doit produire un pavage sur une surface défini par inf_gauche et sup_droit


    inf_gauche, sup_droit:
        des valeurs entières inf_gauche, sup_droit donnant une fenêtre dont le coin inférieur gauche est (inf_gauche,
        inf_gauche) et le coin supérieur droit est (sup_droit, sup_droit) sachant que l’on représente uniquement les
        axes x et y, la hauteur du pavage avant transformation étant égale à 0 ;

    longueur:
        la longueur entre le centre et n’importe quel coin de chaque hexagone avant déformation ;

    col:
        les trois couleurs sous forme de triple col = (col1, col2, col3) ;

    centre:
        le centre de la déformation utile pour la fonction deformation (centre = (x_c, y_c, z_c) ;

    rayon:
        le rayon de la sphère de déformation utile pour la fonction deformation.
    """



    def inside_line(posX, posY, sup_droit, longueur, col, centre, rayon):
        """ Dessine une ligne d'hexagonne avec espace exterieur"""
        while posX+2*longueur <= sup_droit:
            point = (posX + longueur*(1+math.cos(math.pi/3)), posY, 0) #position le point pour le prochain hexagonne
            hexagone(point, longueur, col, centre, rayon) # appel fonction hexagonne
            posX = posX+3*longueur #modifie la posX pour le prochain hexagonne

    def outside_line(posX, posY, sup_droit, longueur, col, centre, rayon):
        """ Dessine une ligne d'hexagonne sans espace exterieur"""
        while posX + longueur <= sup_droit:
            point = (posX, posY, 0)  #position le point pour le prochain hexagonne
            hexagone(point, longueur, col, centre, rayon) # appel fonction hexagonne
            posX = posX + 3 * longueur  #modifie la posX pour le prochain hexagonne

    posY = inf_gauche #définition de la position X
    posX = inf_gauche # définition de la position Y

    while posY+2*longueur*math.sin(math.pi/3) < sup_droit: # boucle pour la création de ligne
        inside_line(posX, posY, sup_droit, longueur, col, centre, rayon) # appel fonction ligne inside
        posY += longueur*math.sin(math.pi/3)  # modification de la position sur l'axe Y
        outside_line(posX, posY, sup_droit, longueur, col, centre, rayon) # appel de la fonction ligne outside
        posY += longueur*math.sin(math.pi/3) # modification de la position sur l'axe Y

    turtle.hideturtle()
    turtle.exitonclick() #fermeture fenetre au click

def hexagone(point, longueur, col, centre, rayon):
    """
    Definition de la fonction hexagone qui produit trois hexagones
        point :
        sous forme d’un triple (tuple de trois composantes) donnant la valeur des trois coordonnées,
        du point avant déformation où l’hexagone doit être peint

        longueur:
        la distance (avant déformation)  entre le centre et n’importe quel coin de l’hexagone

        col :
        tuple  contenant les trois couleurs (col1, col2, col3) qui vont être utilisées pour dessiner les hexagones

        centre:
        point  sous forme de triple (c_x, c_y, c_z) qui donne le centre de la sphère de déformation

        rayon:
        le rayon de la sphère de déformation

    """


    def losange_col_1(col, point, longueur, centre, rayon):
        """
        Dessine le premier losange
        """

        ## définition des différents points de référence du losange
        x, y, z = point

        # definition du deuxieme sommet
        x_bis = x - longueur*math.cos(math.pi/3)
        y_bis = y - longueur*math.sin(math.pi/3)
        point_2 = (x_bis,y_bis,z)

        # definition du troisieme sommet
        x_bis = x + longueur * math.cos(math.pi / 3)
        y_bis = y - longueur * math.sin(math.pi / 3)
        point_3 = (x_bis,y_bis,z)

        # definition du quatrieme sommet
        x_bis = x + longueur
        y_bis = y
        point_4 = (x_bis,y_bis,z)

        # definition de la couleur a utiliser
        turtle.color(col[0], col[0])
        turtle.begin_fill()

        # deformation de la position des points
        point_2 = deformation.deformation(point_2, centre, rayon )
        point_3 = deformation.deformation(point_3, centre, rayon)
        point_4 = deformation.deformation(point_4, centre, rayon)

        #dessin du losange
        trace(point_2, point_3, point_4)

        turtle.end_fill()  # remplissage
        return

    def losange_col_2(col, point, longueur, centre, rayon):
        """
        Dessine le deuxieme losange
        """

        ## définition des différents points de référence du losange
        x, y, z = point

        # definition du deuxieme sommet
        x_bis = x + longueur
        y_bis = y
        point_2 = (x_bis, y_bis, z)

        # definition du troisieme sommet
        x_bis = x + longueur * math.cos(math.pi / 3)
        y_bis = y + longueur * math.sin(math.pi / 3)
        point_3 = (x_bis, y_bis, z)

        # definition du quatrieme sommet
        x_bis = x - longueur * math.cos(math.pi / 3)
        y_bis = y + longueur * math.sin(math.pi / 3)
        point_4 = (x_bis, y_bis, z)

        # definition de la couleur a utiliser
        turtle.color(col[1], col[1])

        # deformation de la position des points
        point_2 = deformation.deformation(point_2, centre, rayon)
        point_3 = deformation.deformation(point_3, centre, rayon)
        point_4 = deformation.deformation(point_4, centre, rayon)

        #dessin du losange
        trace(point_2, point_3, point_4)


        return

    def losange_col_3(col, point, longueur, centre, rayon):
        """
        Dessine le premier losange
        """

        ## définition des différents points de référence du losange
        x, y, z = point

        # definition du deuxieme sommet
        x_bis = x - longueur * math.cos(math.pi / 3)
        y_bis = y + longueur * math.sin(math.pi / 3)
        point_2 = (x_bis, y_bis, z)

        # definition du troisieme sommet
        x_bis = x - longueur
        y_bis = y
        point_3 = (x_bis, y_bis, z)

        # definition du quatrieme sommet
        x_bis = x - longueur * math.cos(math.pi / 3)
        y_bis = y - longueur * math.sin(math.pi / 3)
        point_4 = (x_bis, y_bis, z)

        # definition de la couleur a utiliser
        turtle.color(col[2], col[2])
        turtle.begin_fill()

        # deformation de la position des points
        point_2 = deformation.deformation(point_2, centre, rayon)
        point_3 = deformation.deformation(point_3, centre, rayon)
        point_4 = deformation.deformation(point_4, centre, rayon)

        #dessin du losange
        trace(point_2, point_3, point_4)

        turtle.end_fill()  # remplissage
        return

    def trace(point_2, point_3, point_4):
        """
        Dessin le losange
        """

        turtle.begin_fill()

        # dessin du losange
        turtle.goto(point_2[0], point_2[1])
        turtle.goto(point_3[0], point_3[1])
        turtle.goto(point_4[0], point_4[1])

        turtle.end_fill()  # remplissage



    point_mod = deformation.deformation(point, centre, rayon) #modification du point de reference

    #positionne la tortue pour de dessin et fait le premier losange
    turtle.up()
    turtle.goto(point_mod[0], point_mod[1])
    losange_col_1(col, point, longueur, centre, rayon) # dessin le premier losange
    turtle.down()

    #positionne la tortue pour de dessin et fait le deuxieme losange
    turtle.up()
    turtle.goto(point_mod[0], point_mod[1])
    losange_col_2(col, point, longueur, centre, rayon) #dessin du deuxime losange
    turtle.down()

    #positionne la tortue pour de dessin et fait le troisieme losange
    turtle.up()
    turtle.goto(point_mod[0], point_mod[1])
    losange_col_3(col, point, longueur, centre, rayon) #dessin du troisieme losange
    turtle.down()

    return


"""
    Code principal
"""

### mise en place des inputs


inf_gauche = int(input("Entrez la valeur définissant le point en bas à gauche de la toile"))
sup_droit = int(input("Entrez la valeur définissant le point en haut à droite de la toile"))
longueur = int(input("Entrez la valeur définissant la longueur d'un côté de l'hexagone"))

col1 = str(input("Entrez le nonm de couleur définissant le premier losange"))
col2 = str(input("Entrez le nom couleur définissant le deuxième losange"))
col3 = str(input("Entrez le nom couleur définissant le troisième losange"))


col = (col1, col2, col3) #création d'un tuple de couleur



cx = int(input("Entrez la position sur l'axe X du centre du cercle"))
cy = int(input("Entrez la position sur l'axe Y du centre du cercle"))
cz = 0
centre = (cx, cy, cz) #création d'un tuple pour les coordonnées


rayon = int(input("Entrez le rayon du cencle de déformation"))

pavage(inf_gauche, sup_droit, longueur, col, centre, rayon) # appel de la fonction qui lance le dessin


