"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé



Cet exercice propose une variante de l’exercice précédent sur le carré de X.

Écrire un programme qui lit sur input une valeur naturelle n et qui affiche à l’écran un triangle supérieur
droit formé de X (voir exemples plus bas).





"""
n = int(input())

for i in range(n):
    if i == 0:
        print("X" * (n-i))
    else:
        print(" "*(i-1), "X"*(n-i))
