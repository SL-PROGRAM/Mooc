"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Écrire une fonction prime_odd_numbers(numbers) qui reçoit une liste de nombres et qui renvoie un couple d’ensembles
contenant respectivement les nombres premiers présents dans la liste et les nombres impairs.

Pour cela, nous vons demandons d’écrire deux fonctions annexes qui seront appelées dans le corps de la fonction
prime_odd_numbers :

    la fonction even(max_nb) qui renvoie l’ensemble des nombres naturels pairs inférieurs ou égaux à max_nb

    la fonction prime_numbers(max_nb) qui renvoie l’ensemble des nombres premiers inférieurs ou égaux à max_nb.


Consignes

Dans cet exercice, il vous est demandé d’écrire seulement des fonctions.

Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en
particulier aucun appel à input ou à print.

"""

def prime_odd_numbers(numbers):
    def even(max_nb):
        even = set()
        for elem in max_nb:
            if elem % 2 == 0:
                even.add(elem)
        return even

    def prime_numbers(max_nb):
        lst_prime = set()
        for elem in max_nb:
            prime = True
            nb_prime = elem
            if elem <= 1:
                prime = False
            for i in range(2, elem):
                if elem % i == 0:
                    prime = False
            if prime == True:
                lst_prime.add(nb_prime)
        return lst_prime

    prime = prime_numbers(numbers)
    lst_even =  even(numbers)
    odd = set(numbers)- set(lst_even)
    return (prime, odd)

print(prime_odd_numbers([1, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97]))


