"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Écrire une fonction alea_dice(s) qui génère trois nombres (pseudo) aléatoires à l’aide de la fonction randint du module
 random, représentant trois dés (à six faces avec les valeurs de 1 à 6), et qui renvoie la valeur booléenne True si
 les dés forment un 421, et la valeur booléenne False sinon.

Le paramètre s de la fonction est un nombre entier, qui sera passé en argument à la fonction random.seed au début
du code de la fonction. Cela permettra de générer la même suite de nombres aléatoires à chaque appel de la fonction,
et ainsi de pouvoir tester son fonctionnement.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction alea_dice. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.

    Il n’est pas demandé que la fonction alea_dice teste le type du paramètre reçu.

    N’importe quelle combinaison de trois dés permettant de former le nombre 421 sera acceptée, quel que soit l’ordre
    de la combinaison. Par exemple, les tirages 2, 4, 1 forment bien 421.

    La première instruction de la fonction, après l’import du module random, sera random.seed(s).

    On rappelle que la fonction randint(a, b) retourne un nombre (pseudo) aléatoire compris entre les bornes a et b
    incluses.


"""

def alea_dice(s):
    import random
    random.seed(s)
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    test = False
    if (a, b, c) == (1, 2, 4) or (a, b, c) == (1, 4, 2) or (a, b, c) == (2, 1, 4)\
            or (a, b, c) == (2, 4, 1) or (a, b, c) == (4, 1, 2) or (a, b, c) == (4, 2, 1):
        test = True
    return test

print(alea_dice(1))