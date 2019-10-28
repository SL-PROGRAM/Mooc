"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Écrire un programme qui lit sur input une valeur naturelle n et qui affiche à l’écran un carré de
n caractères X (majuscule) de côté.





"""

n = int(input())

for i in range(n):
    print("X" * n)
