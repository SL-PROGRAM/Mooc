"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé



Écrire une fonction booléenne premier(n) qui reçoit un nombre entier positif n et qui renvoie True si n est un nombre
premier, et False sinon.

Ensuite, écrire un programme qui lit une valeur entière x et affiche, grâce à des appels à la fonction premier, tous
les nombres premiers strictement inférieurs à x, chacun sur sa propre ligne.


Consignes

    Dans cet exercice, il vous est demandé d’écrire une fonction, puis un programme appelant cette fonction.
    Notez qu’UpyLaB testera ces deux points, en exécutant le programme entier mais aussi en appelant directement la
    fonction avec les arguments de son choix.

    Il n’est pas demandé que la fonction premier teste le type du paramètre reçu, ni si sa valeur est bien positive ou
    nulle.

    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer, ou
    pour les fonctions ne renvoyer, que le résultat attendu. En particulier, il ne faut rien écrire à l’intérieur des
    appels à input (int(input()) et non int(input("Entrer un nombre : ") par exemple), ni ajouter du texte dans ce qui
    est imprimé (print(res) et non print("résultat :", res) par exemple).

"""


def premier(n):
    test = True

    if n == 0 or n == 1:
        test = False

    for i in range(n):
        if i == 0 or i == 1:
            pass
        elif n%i == 0:
            test = False

    return test

n = int(input())

for i in range(n):
    if i == 0 or i == 1:
        pass
    elif premier(i) == True:
        print(i)
