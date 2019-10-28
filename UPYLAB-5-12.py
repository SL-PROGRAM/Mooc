"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Enoncé



Écrire une fonction my_insert qui reçoit comme premier paramètre une liste triée d’entiers par ordre croissant et comme
deuxième paramètre un entier n, et qui renvoie une liste correspondant à la liste reçue, mais dans laquelle le nombre
n a été inséré à la bonne place.

La liste donnée en paramètre ne doit pas être modifiée par votre fonction.

Vous pouvez supposer que le premier paramètre sera bien une liste triée d’entiers, mais si le deuxième paramètre
n’est pas du bon type, la fonction retourne None.


Consignes

Dans cet exercice, il vous est demandé d’écrire seulement la fonction my_insert.

Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en
particulier aucun appel à input ou à print.



"""

def my_insert(liste, n):
    new_liste = liste.copy()
    if type(liste) != list or type(n) != int:
        new_liste = None
    else:
        for i in liste:
            if i > n:
                pos = liste.index(i)
                new_liste.insert(pos, n)
                break
    return new_liste

print(my_insert([1,2,4],3))


