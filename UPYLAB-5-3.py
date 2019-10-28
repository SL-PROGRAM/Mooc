"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Écrire une fonction duree qui reçoit deux paramètres debut et fin. Ces derniers sont des couples (tuples de deux
composantes) dont la première composante représente une heure et la seconde les minutes.

Cette fonction doit calculer la durée qui s’est écoulée entre ces deux instants. Le résultat sera donné sous
la forme d’un tuple (heure, minutes).


"""

def duree(duree1, duree2):

    import math
    h1, m1 = duree1
    h2, m2 = duree2

    temps1 = h1*60+m1
    temps2 = h2*60+m2

    temps = abs(temps1 - temps2)
    h = temps //60
    m = temps %60

    if temps1 > temps2:
        #23 heure + 1h en minute
        h = 23-h
        m = 60 -m


    return h,m

print(duree((11, 48), (4, 40)) )