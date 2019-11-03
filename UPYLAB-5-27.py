"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Écrire une fonction symetrie_horizontale(A) qui reçoit une matrice carrée A (de taille {n}\times{n}) et qui renvoie
l’image de A par symétrie horizontale par rapport à la ligne du milieu : la première ligne devenant la dernière, la
seconde, l’avant-dernière, etc.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction symetrie_horizontale. Le code que vous
    soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier
    aucun appel à input ou à print.

    Vous pourrez supposer que les matrices passées en argument sont bien carrées (même nombre de lignes et de colonnes).



"""


def symetrie_horizontale(M):
    sym_M = []
    for i in range(len(M)):
        sym_M += [M[len(M)-1-i]]

    return sym_M

print(symetrie_horizontale([[0, -4, -1, -6, -4, -7],
                      [4, 0, -8, -2, -6, -10],
                      [1, 8, 0, -4, -7, -3],
                      [6, 2, 4, 0, -9, -5],
                      [4, 6, 7, 9, 0, 0],
                      [7, 10, 3, 5, 0, 0]]))