"""Auteur: Simon LEYRAL
   Date : Octobre 2017
 Enoncé

Le but de cet exercice est de vous familiariser avec la syntaxe Python pour écrire des expressions arithmétiques
simples et avec l’instruction print qui affiche (on dit aussi imprime) des valeurs à l’écran.

Écrire un programme qui lit deux valeurs entières x et y strictement positives suivies de deux valeurs
réelles (float) z et t, et qui affiche les valeurs des expressions suivantes, chacune sur une nouvelle ligne
"""
x = int(input())
y = int(input())
z = float(input())
t = float(input())

print(x - y)
print(x +z)
print(z + t)
print(x * z)
print(x / 2)
print(x/(y+1))
print((x+y)*z/(4*x))
print(x**(-1/2))
