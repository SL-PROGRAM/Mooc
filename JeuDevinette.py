"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Jeu de devinette Version 1

Consignes : le programme :

    choisit aléatoirement un nombre entre 0 et 5 sans en afficher la valeur (et donc sans que l’utilisateur connaisse cette valeur) et le place dans la variable secret ;

    demande à l’utilisateur de deviner la valeur choisie ;

    affiche "gagné !" si l’utilisateur trouve la bonne réponse et

    affiche "perdu !  La valeur était " suivi de la valeur de secret dans le cas contraire.



"""
import random

secret = random.randint(0, 5)


x =int(input("entrer un nmbre entre 0 et 5"))

if x == secret:
    print("gagné")
else:
    print("perdu ! La valeur était ", secret)

