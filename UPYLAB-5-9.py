"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Enoncé

Écrire une fonction intersection(v, w) qui calcule l’intersection entre deux chaînes de caractères v et w.

On définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots. Par exemple,
l’intersection de « programme » et « grammaire » est « gramm ».

Si les deux chaînes n’ont aucun caractère en commun, la fonction retourne la chaîne vide, ''.

Si plusieurs solutions sont possibles, la fonction retournera la sous-chaîne d’indice minimal dans v. Par exemple,
intersection('bbaacc', 'aabb') renvoie 'bb'.


Consignes

Dans cet exercice, il vous est demandé d’écrire seulement la fonction intersection.

Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
et ne fait en particulier aucun appel à input ou à print.


"""

def intersection(v,w):
    inter = ""
    for i in range(len(v)+1):
        for j in (range(len(v)+1)):
            if v[i:j] in w and len(v[i:j]) > len(inter) :
                inter = v[i:j]
    return inter

print(intersection('crane', 'carne'))

