"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Écrire un programme qui lit 3 nombres entiers, et qui, si au moins deux d’entre eux ont la même valeur,
imprime cette valeur (le programme n’imprime rien dans le cas contraire).



"""
val1 =int(input())
val2 =int(input())
val3 =int(input())

if val1 == val2 or val1 == val3:
    print(val1)
elif val2 == val3:
    print(val2)
