"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé


Écrire un programme qui additionne des valeurs naturelles lues sur input et affiche le résultat.

La première donnée lue ne fait pas partie des valeurs à sommer. Elle détermine si la liste contient un nombre
déterminé à l’avance de valeurs à lire ou non :

    si cette valeur est un nombre positif ou nul, elle donne le nombre de valeurs à lire et à sommer ;

    si elle est négative, cela signifie qu’elle est suivie d’une liste de données à lire qui sera terminée par
    le caractère "F" signifiant que la liste est terminée.




"""
n = int(input())
somme = 0
if n >= 0:
    for i in range(n):
        nb = int(input())
        somme += nb
else:
    nb = 0
    while(nb != "F"):
        nb = input()
        if nb != "F":
            somme += int(nb)


print(somme)
