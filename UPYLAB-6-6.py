"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Écrire une fonction valeurs(dico) qui doit fournir, à partir du dictionnaire donné en paramètre, une liste des valeurs
du dictionnaire triées selon leur clé.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction valeurs. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à
    print.

    Vous pourrez supposer que les clés du dictionnaire sont des chaînes de caractères.


"""

def valeurs(dico):
    lst =[]
    lst_cle = []
    for cle in dico:
        lst_cle.append(cle)

    lst_cle.sort()
    print(lst_cle)
    for elem in lst_cle:
        lst.append(dico[elem])
    return lst