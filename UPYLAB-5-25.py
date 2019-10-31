"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Enoncé

Écrire une fonction trace(M) qui reçoit en paramètre une matrice M de taille {n}\times{n} contenant des valeurs
numériques (de type int ou float), et qui renvoie sa trace, c’est-à-dire la somme de tous les éléments de la première
diagonale.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction trace. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à
    print.

    Les éléments de la première diagonale sont les éléments dont l’indice de ligne est égal à l’indice de colonne.
    Ainsi :

trace(M) = \sum_{i = 0}^{n - 1} m_{ii}

    Vous pourrez supposer que les matrices passées en argument seront bien carrées (même nombre de lignes et de
    colonnes).






"""


def trace(M):
    som = 0
    for i in range(len(M)):
        som += M[i][i]

    return som

trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]])