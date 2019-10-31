"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Enoncé

Écrire une fonction init_mat(m, n) qui construit et renvoie une matrice d’entiers initialisée à la matrice nulle et
de dimension m x n.



Consignes

Dans cet exercice, il vous est demandé d’écrire seulement la fonction init_mat.

Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en
particulier aucun appel à input ou à print.



"""


def init_mat(m, n):
    matrice = []
    for i in range(m):
        matrice.append([])
        for j in range(n):
            matrice[i].append(0)
    return matrice

print(init_mat(2,3))