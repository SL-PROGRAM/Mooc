"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Enoncé

L’exercice est le même que le précédent, mais ici, si les paramètres ont le type attendu, la fonction modifie la liste
en place et ne retourne rien. Si les paramètres ne sont pas valides, une erreur se produit à l’exécution.

Énonce précedent:

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
    assert type(liste) == list or type(n) == int
    for i in liste:
        if i > n:
            pos = liste.index(i)
            liste.insert(pos, n)
            break


print(my_insert([1, 2, 4], 3))
