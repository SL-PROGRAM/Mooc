"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Énoncé



On considère une liste qui décrit une séquence t. Chaque élément de cette liste est un tuple de deux composantes : le
nombre de répétitions successives de l’élément x dans la séquence t, et l’élément x lui-même.

Par exemple, la liste [(1, 'He'), (2, 'l'), (1,'o')] décrit la séquence "Hello".

Écrire une fonction decompresse qui reçoit une telle liste en paramètre et renvoie la séquence t sous forme d’une
nouvelle liste.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction decompresse. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.

    Essayez d’utiliser une compréhension de liste pour cet exercice.




"""


def decompresse(lst):
    t = [ y for (x,y) in lst for x in range(x)]
    return t

print(decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]))