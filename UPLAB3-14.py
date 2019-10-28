"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret) compris entre 0 et 100. Ensuite,
le joueur doit deviner ce nombre en utilisant le moins d’essais possible.

À chaque tour, le joueur est invité à proposer un nombre et le programme doit donner une réponse parmi les suivantes :

    « Trop grand » : si le nombre secret est plus petit que la proposition et qu’on n’est pas au maximum d’essais

    « Trop petit » : si le nombre secret est plus grand que la proposition et qu’on n’est pas au maximum d’essais

    « Gagné en n essais ! » : si le nombre secret est trouvé

    « Perdu ! Le secret était nombre » : si le joueur a utilisé six essais sans trouver le nombre secret.




"""
import random

secret = random.randint(0, 100)
essai =0
x= 0

while(essai < 6 and x != secret):
    x =int(input())
    essai += 1
    if x == secret:
        print("gagné en", essai, "essais !")
    elif essai > 5:
        print("perdu ! Le secret était", secret)
    elif x < secret:
        print("Trop petit")
    else:
        print("Trop grand")



