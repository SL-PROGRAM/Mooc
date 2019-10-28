"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Écrire un programme qui imprime la moyenne géométrique \sqrt{a.b} (la racine carrée du produit de a par b) de deux nombres positifs a et b de type float lus en entrée.

Si au moins un de ces nombres est strictement négatif, le programme imprime le texte « Erreur ».



"""
from math import sqrt
poly = input()
long = float(input())

if poly == "T":
    print(sqrt(2)/12*long**3)
elif poly == "C":
    print(long**3)
elif poly == "O":
    print(sqrt(2)/3*long**3)
elif poly == "D":
    print((15+7*sqrt(5))/4*long**3)
elif poly == "I":
    print(5*(3+sqrt(5))*long**3/12)
else:
    print("Polyèdre non connu")