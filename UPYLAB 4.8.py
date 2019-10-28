"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Dans cet exercice, nous allons mettre en pratique la notion de valeur par défaut des paramètres d’une fonction.

Écrire une fonction somme(a, b) qui retourne la somme de deux valeurs entières a et b. Par défaut,
la valeur de a est 0 et la valeur de b est 1.




Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction somme. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.

    Il n’est pas demandé que la fonction somme teste le type des paramètres reçus.



"""

def somme(a = 0, b = 1):
    return a+b
