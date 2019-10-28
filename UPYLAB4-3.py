"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé



Écrire une fonction fibo(n) qui reçoit un nombre entier n et qui renvoie la valeur du nombre de Fibonacci F_n.

On rappelle que :

        F_0 vaut 0 ;

        F_1 vaut 1 ;

        F_{i + 1} vaut F_i + F_{i-1} pour i > 0 ;

        F_i vaut None pour i < 0.

Ensuite, écrire un programme qui lit une valeur entière strictement positive x et affiche le résultat de fibo(i)
pour i allant de 0 compris à x non compris, avec chaque valeur sur sa propre ligne.



"""


def fibo(i):
    fibo = 0
    fibo1 = 1
    if i < 0:
        return None
    if i == 0:
        return fibo
    elif i == 1:
        return fibo1
    else:
        for a in range(i):
            fibo, fibo1 = fibo+fibo1, fibo
        return fibo

x = int(input())
for a in range(x):
    print(fibo(a))

