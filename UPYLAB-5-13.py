"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Enoncé



Écrire une fonction my_count qui reçoit une liste lst et un élément e en paramètres.

La fonction doit renvoyer le nombre de fois où l’élément e apparaît dans la liste. Si lst n’est pas du bon type, la
 fonction retourne la valeur 0.



Consignes

Dans cet exercice, il vous est demandé d’écrire seulement la fonction my_count.

Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en
particulier aucun appel à input ou à print.


"""

def my_count(lst, e):
    if type(lst) != list:
        elem = 0
    else:
        elem=0
        for i in lst:
            if i == e:
                elem +=1

    return elem

