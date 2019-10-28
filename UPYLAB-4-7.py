"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Considérons les billets et pièces de valeurs suivantes : 20 euros, 10 euros, 5 euros, 2 euros et 1 euro.

Écrire une fonction rendre_monnaie qui reçoit en paramètre un entier prix et cinq valeurs entières x20, x10, x5, x2
et x1, qui représentent le nombre de billets ou de pièces de chaque valeur que donne un client pour l’achat d’un objet
dont le prix est mentionné.

La fonction doit renvoyer cinq valeurs, représentant le nombre de billets et pièces de chaque sorte qu’il faut rendre
au client, dans le même ordre que précédemment. Cette décomposition doit être faite en rendant le plus possible de
billets et pièces de grosses valeurs.

Si la somme d’argent avancée par le client n’est pas suffisante pour effectuer l’achat, la fonction retournera cinq
valeurs None.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction rendre_monnaie. Le code que vous soumettez
    à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun
    appel à input ou à print.

    Il n’est pas demandé que la fonction rendre_monnaie teste le type des paramètres reçus.

    On suppose qu’il y a toujours suffisamment de billets et pièces de chaque sorte.

    Pour retourner cinq valeurs, on pourra utiliser l’instruction return res20, res10, res5, res2, res1.
    Cela renvoie un tuple de cinq valeurs (apparaissant entre parenthèses lorsqu’on l’affiche).


"""

def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    if prix > (20*x20 + 10*x10 + 5*x5 + 2*x2 + x1):
        rendu = (None, None, None, None, None)
    elif prix == (20*x20 + 10*x10 + 5*x5 + 2*x2 + x1):
        rendu = (0, 0, 0, 0, 0)
    else:
        a_rendre = (20*x20 + 10*x10 + 5*x5 + 2*x2 + x1) - prix
        res20 = a_rendre//20
        a_rendre -= 20*res20
        res10 = a_rendre//10
        a_rendre -= 10*res10
        res5 = a_rendre//5
        a_rendre -= 5 * res5
        res2 = a_rendre//2
        a_rendre -= 2 * res2
        res1 = a_rendre
        rendu = (res20, res10, res5, res2, res1)
    return rendu
