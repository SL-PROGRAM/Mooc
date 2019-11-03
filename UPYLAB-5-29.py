"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

(D’après une idée de Jacky Trinh le 15/02/2018)

Puissance 4 est un jeu de stratégie combinatoire abstrait dont le but est d’aligner une suite de quatre pions de même
couleur sur une grille comptant six rangées et sept colonnes.

Chaque joueur possède vingt-et-un pions d’une couleur (jaune ou rouge). À chaque tour, le joueur suivant doit placer un
 pion dans la colonne de son choix. Le pion tombe dans la position la plus basse possible.

Le vainqueur est le premier qui a réussi à aligner horizontalement, verticalement ou diagonalement, de manière
consécutive, quatre de ses pions.

Écrire une fonction gagnant(grille) où grille est la grille de jeu sous forme de matrice.

Cette matrice contient donc six listes de lignes contenant chacune sept éléments.

La ligne à l’indice 0 représente le bas du jeu.

Les éléments de cette matrice seront soit 'R', soit 'J' ou soit 'V' pour un emplacement encore vide.

Cette fonction renverra 'R' si le joueur à la couleur rouge a gagné, 'J' si le joueur à la couleur jaune a gagné ou
bien None si aucun joueur n’a gagné.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction gagnant. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à
    print.

    Vous pourrez supposer que la matrice passée à la fonction est valide, et qu’il n’y a pas à la fois une
    configuration gagnante pour chacune des couleurs.


"""

def gagnant(grille):
    vainqueur = None
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if j +3 <= len(grille[i]) and grille[i][j] != "V" and grille[i][j] == grille[i][j+1] and grille[i][j+1] == grille[i][j+2] \
                    and grille[i][j+2] == grille[i][j+3]:
                vainqueur = grille[i][j]
                break
            if i +3 <= len(grille):
                if grille[i][j] != "V" and grille[i][j] == grille[i+1][j] and grille[i+1][j] == grille[i+2][j] \
                        and grille[i+2][j] == grille[i+3][j]:
                    vainqueur = grille[i][j]
                    break
                elif j +3 <= len(grille[i]) and grille[i][j] != "V" and grille[i][j] == grille[i+1][j+1] and grille[i+1][j+1] == grille[i+2][j+2] \
                        and grille[i+2][j+2] == grille[i+3][j+3]:
                    vainqueur = grille[i][j]
                    break
            if i-3>= 0:
                if j - 3 >= 0 and grille[i][j] != "V" and grille[i][j] == grille[i - 1][j - 1] and grille[i - 1][j - 1] == \
                        grille[i - 2][j - 2] and grille[i - 2][j - 2] == grille[i - 3][j - 3]:
                    vainqueur = grille[i][j]
                    break
                elif j +3 <= len(grille[i]) and grille[i][j] != "V" and grille[i][j] == grille[i-1][j+1] and grille[i-1][j+1] == grille[i-2][j+2] \
                        and grille[i-2][j+2] == grille[i-3][j+3]:
                    vainqueur = grille[i][j]
                    break
    return vainqueur

print(gagnant([['J', 'R', 'J', 'J', 'R', 'R', 'J'],
               ['V', 'R', 'R', 'J', 'J', 'R', 'R'],
               ['V', 'R', 'J', 'J', 'R', 'J', 'R'],
               ['V', 'J', 'R', 'J', 'V', 'V', 'V'],
               ['V', 'R', 'J', 'V', 'V', 'V', 'V'],
               ['V', 'J', 'R', 'V', 'V', 'V', 'V']]))


print(gagnant([['J', 'J', 'R', 'J', 'J', 'J', 'J'],
               ['R', 'V', 'J', 'R', 'V', 'J', 'R'],
               ['R', 'V', 'J', 'R', 'V', 'J', 'R'],
               ['V', 'V', 'V', 'J', 'V', 'R', 'R'],
               ['V', 'V', 'V', 'R', 'V', 'V', 'V'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))