"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Nous vous proposons d’écrire deux petits programmes qui calculent et impriment les premiers termes
de la suite de Fibonacci dans deux cas de figure :

    problème 1 : pour les n premiers termes

    problème 2 : pour tous les termes inférie urs à une valeur n donnée.



"""

prec = 0
succ = 1
n = int(input())

#probleme 1
print(prec, end= " ")
print(succ, end = " ")
for i in range(n-2):
    prec, succ = succ, prec+ succ
    print(succ, end = " ")
print()

#probleme 2

prec = 0
succ = 1
n = int(input())

print(prec, end= " ")
while succ < n:
    print(succ, end=" ")
    prec, succ = succ, prec+ succ
print()
