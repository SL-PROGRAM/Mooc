"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Écrire une fonction construction_dict_amis qui reçoit une liste de couples (prenom1, prenom2) signifiant que prenom1
déclare prenom2 comme étant son ami.

La fonction construit et renvoie un dictionnaire dont les clés sont les prénoms des personnes nommées, et la valeur de
chaque entrée est l’ensemble des amis de la personne.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction construction_dict_amis. Le code que vous
    soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier
    aucun appel à input ou à print.

    Si, dans la liste reçue, nous avons le couple (prenom1, prenom2), cela n’induit pas que prenom1 figure parmi les
    amis de prenom2. Si le couple (prenom2, prenom1) n’est pas dans cette liste, nous aurons une amitié à sens unique !

    Vous pourrez supposer que les arguments passés à la fonction sont du bon type.




"""

def construction_dict_amis(lst):
    d = {}
    for prenom1, prenom2 in lst:
        if prenom1 in d :
            d[prenom1].add(prenom2)
        else:
            d[prenom1] = {prenom2}
        if prenom2 not in d:
            d[prenom2] = set()
    return d

print(construction_dict_amis([('Quidam', 'Pierre'),
                        ('Thierry', 'Michelle'),
                        ('Thierry', 'Pierre')]))