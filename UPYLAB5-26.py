"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Enoncé



Une matrice M = \{m_{ij}\} de taille {n}\times{n} est dite antisymétrique lorsque, pour toute paire d’indices i, j,
 on a m_{ij} = - m_{ji}.

Écrire une fonction booléenne antisymetrique(M) qui teste si la matrice M reçue est antisymétrique.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction antisymetrique. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.

    Vous pourrez supposer que les matrices passées en argument sont bien carrées (même nombre de lignes et de colonnes).

    On rappelle qu’une fonction booléenne retourne les valeurs True ou False.

    La fonction retourne True pour la matrice vide.



"""


def antisymetrique(M):
    test = True
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[j][i] != -M[i][j]:
                test = False

    return test

print(antisymetrique([[0, -4, -1, -6, -4, -7],
                      [4, 0, -8, -2, -6, -10],
                      [1, 8, 0, -4, -7, -3],
                      [6, 2, 4, 0, -9, -5],
                      [4, 6, 7, 9, 0, 0],
                      [7, 10, 3, 5, 0, 0]]))