"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Écrire une fonction symetrise_amis qui reçoit un dictionnaire d d’amis où les clés sont des prénoms et les valeurs, des
ensembles de prénoms représentant les amis de chacun.

Cette fonction modifie le dictionnaire d de sorte que si une clé prenom1 contient prenom2 dans l’ensemble de ses amis,
l’inverse soit vrai aussi.

La fonction accepte un second paramètre englobe.

Si englobe est vrai, la fonction ajoutera les éléments nécessaires pour symétriser le dictionnaire d.

Sinon, la fonction enlèvera les éléments nécessaires pour symétriser d.



Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction symetrise_amis. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input
     ou à print.

    Notez que les prénoms figurant dans les ensembles d’amis font eux-même partie des clés du dictionnaire d.

    Vous pourrez supposer que les arguments passés à la fonction sont du bon type.




"""

def symetrise_amis(d, englobe):
    supp = []
    for cle in d:
        for elem in d[cle]:
            if cle not in d[elem]:
                if englobe:
                    d[elem].add(cle)
                else:
                    supp += [elem]
        if not englobe and supp != []:
            for sup in supp:
                d[cle].remove(sup)
                supp = []


d = {'Pierre': set(), 'Thierry': {'Ariane', 'Bernadette'}, 'Bernadette': set(), 'Ariane': {'Pierre', 'Quidam'}, 'Quidam': set()}
symetrise_amis(d, False)
print(d)