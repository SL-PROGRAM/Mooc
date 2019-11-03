"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

(D’après une idée de Jacky Trinh le 15/02/2018)

Puissance 4 est un jeu de stratégie combinatoire abstrait dont le but est d’aligner une suite de quatre pions de même
couleur sur une grille comptant six rangées et sept colonnes.

Chaque joueur possède vingt-et-un pions d’une couleur (jaune ou rouge). À chaque tour, le joueur suivant doit placer
un pion dans la colonne de son choix. Le pion tombe dans la position la plus basse possible.

Le vainqueur est le premier qui a réussi à aligner horizontalement, verticalement ou diagonalement, de manière
consécutive, quatre de ses pions.

Écrire une fonction placer_pion(couleur, colonne, grille) où :

    couleur est la couleur du pion, qui peut être soit 'R' (rouge), soit 'J' (jaune),

    colonne est l’indice de la colonne où le joueur souhaite placer le pion (allant de 0 à 6),

    grille est la grille de jeu sous forme de matrice.

Cette matrice contient donc six listes de lignes contenant chacune sept éléments.

La ligne à l’indice 0 représente le bas du jeu.

Les éléments de cette matrice seront soit 'R', soit 'J' ou soit 'V' pour un emplacement encore vide.

Cette fonction placera un pion dans la grille du jeu et renverra un couple de valeurs :

    si le placement est possible, la valeur booléenne True et la grille modifiée,

    sinon, la valeur booléenne False et la grille non modifiée.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction placer_pion. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.

    Vous pourrez supposer que les arguments passés à la fonction seront valides.

    Il n’est pas demandé de vérifier si la grille contient un alignement gagnant.

"""

def placer_pion(couleur, colonne, grille):
    test = False
    for i in range(len(grille)):
        if grille[i][colonne] == "V":
            grille[i][colonne] = couleur
            test = True
            break
    return test, grille
