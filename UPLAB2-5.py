"""Auteur: Simon LEYRAL
   Date : Octobre 2017
 Enoncé

Écrire un programme qui lit une longueur long de type float strictement positive, et qui affiche les valeurs x y des
coordonnées (x, y) des sommets de l’hexagone de centre (0,0) et de rayon long

"""

from math import pi, cos, sin

long = float(input())

x = long
y = 0


print(x, y)
x = long*cos(pi/3)
y = long*sin(pi/3)
print(x, y)

x = -long*cos(pi/3)
y = long*sin(pi/3)
print(x, y)

x = -long
y=0
print(x, y)

x = -long*cos(pi/3)
y = -long*sin(pi/3)
print(x, y)

x = long*cos(pi/3)
y = -long*sin(pi/3)
print(x,y)