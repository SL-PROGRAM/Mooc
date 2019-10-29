"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Énoncé

Écrire une fonction my_filter qui reçoit une liste lst et une fonction booléenne f en paramètres et renvoie une
nouvelle liste constituée des éléments de lst pour lesquels la fonction f renvoie True.

Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction my_filter. Le code que vous soumettez à UpyLaB
     doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
     input ou à print.

    On rappelle qu’une fonction booléenne est une fonction qui retourne True ou False.

    Essayez d’utiliser une compréhension de liste pour cet exercice.

"""


def my_filter(lst, f):
    t = [ elem for elem in lst if f(elem) == True]
    return t


print(my_filter(['hello', 666, 42, 'Thierry', 1.5], lambda x : isinstance(x, int)))