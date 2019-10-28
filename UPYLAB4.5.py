"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Écrire une fonction rac_eq_2nd_deg(a, b, c) qui reçoit trois paramètres de type float correspondant aux trois
coefficients de l’équation du second degré ax^2 + bx + c = 0, et qui renvoie la ou les solutions s’il y en a,
sous forme d’un tuple.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction rac_eq_2nd_deg. Le code que vous soumettez
    à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.

    Il n’est pas demandé que la fonction rac_eq_2nd_deg teste le type des paramètres reçus.

    Le résultat retourné par la fonction rac_eq_2nd_deg est un tuple.

            S’il n’y a pas de solution réelle, elle retourne un tuple vide tuple().

            S’il y a une unique racine r1, elle retourne le tuple (r1,).

            S’il y a deux solutions réelles, r1 et r2, la plus petite des deux devra être la première composante du
            tuple retourné (composante d’indice 0). La fonction pourra retourner le tuple (min(r1, r2), max(r1, r2)).


"""


def rac_eq_2nd_deg(a, b, c):
    import math
    delta = b*b - 4*a*c
    solution = tuple()
    if delta == 0:
        solution = (-b/(2*a), )
    elif delta > 0:
        sol1 = (-b-math.sqrt(delta))/(2*a)
        sol2 = (-b+math.sqrt(delta))/(2*a)
        solution = min(sol1, sol2), max(sol1, sol2)
    return solution

print(rac_eq_2nd_deg(1.0, -4.0, 4.0))