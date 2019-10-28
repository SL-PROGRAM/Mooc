"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Enoncé





Écrire une fonction my_remove qui reçoit une liste lst et un élément e en paramètres.

La fonction efface la première apparition de l’élément e dans la liste et ne renvoie rien.

Si lst n’est pas une liste, la fonction ne fait rien.


Consignes

Dans cet exercice, il vous est demandé d’écrire seulement la fonction my_remove.

Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
et ne fait en particulier aucun appel à input ou à print.


"""

def my_remove(lst, e):
    if type(lst) !=list or type(e) != int:
        pass
    else:
        pos = lst.index(e)
        lst.pop(pos)