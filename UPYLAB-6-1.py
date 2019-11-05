"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

(D’après une idée de Jacky Trinh le 19/02/2018)

Monsieur Germain est une personne très âgée. Il aimerait préparer une liste de courses à faire à l’avance. Ayant un
budget assez serré, il voudrait que sa liste de courses soit dans ses capacités. Son seul petit souci est qu’il a une
très mauvaise vue et n’arrive donc pas à voir le prix associé à chaque produit contenu dans le catalogue de courses.

Écrire une fonction calcul_prix(produits, catalogue) où :

    produits est un dictionnaire contenant, comme clés, les produits souhaités par Monsieur Germain et comme valeurs
    associées, la quantité désirée de chacun d’entre eux,

    catalogue est une dictionnaire contenant tous les produits du magasin avec leur prix associé.

La fonction retourne le montant total des achats de Monsieur Germain.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction calcul_prix. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.

    Vous pourrez supposer que les arguments passés à la fonction sont du bon type, et que les produits souhaités par
    Monsieur Germain figurent bien dans le catalogue du magasin.



"""

def calcul_prix(produits, catalogue):
    tot = 0
    for cle in produits:
        tot += produits[cle]*catalogue[cle]

    return tot

print(calcul_prix({"brocoli":2, "mouchoirs":5, "bouteilles d'eau":6},
            {"brocoli":1.50, "bouteilles d'eau":1, "bière":2,
             "savon":2.50, "mouchoirs":0.80}))