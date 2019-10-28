"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé


Nous vous demandons :

    d’écrire une fonction catalan(n), où n est un nombre entier positif ou nul, qui renvoie la valeur du n-ième
    nombre de Catalan.

    puis d’écrire un programme qui lit la valeur de n (int) sur input, et affiche le résultat de votre
    fonction appelée avec le paramètre n.

Le nombre de Catalan d’indice n, appelé n-ième nombre de Catalan, est défini par :

C_n = \frac{(2n)!}{(n+1)!n!}


"""
import math

def catalan(n):
    return int(math.factorial(2*n)/(math.factorial(n+1)*math.factorial(n)))

n = int(input())
print(catalan(n))
