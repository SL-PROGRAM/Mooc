"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

(D’après une idée de Jacky Trinh le 24/02/2018)

Un jury doit attribuer le prix du « Codeur de l’année ».

Afin de récompenser les trois candidats ayant obtenu la meilleure moyenne, nous vous demandons d’écrire une fonction
top_3_candidats(moyennes) qui reçoit un dictionnaire contenant comme clés les noms des candidats et comme valeurs la
moyenne que chacun a obtenue.

Cette fonction doit retourner un tuple contenant les noms des trois meilleurs candidats, par ordre décroissant de
leurs moyennes.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction top_3_candidats. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.

    Vous pourrez supposer que l’argument passé à la fonction est du bon type.

    Vous pourrez supposer que les candidats ont des moyennes différentes, et qu’ils sont plus de trois.



"""

def top_3_candidats(moyennes):
    prem = 0
    deux = 0
    trois = 0
    c_prem =""
    c_deux =""
    c_trois =""
    for i in moyennes:
        if moyennes[i] > prem:
            trois = deux
            c_trois = c_deux
            c_deux = c_prem
            deux = prem
            prem = moyennes[i]
            c_prem = i
        elif moyennes[i]> deux:
            trois = deux
            c_trois = c_deux
            deux = moyennes[i]
            c_deux = i
        elif moyennes[i] > trois:
            trois = moyennes[i]
            c_trois = i

    return (c_prem, c_deux, c_trois)

print(top_3_candidats({'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
                 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
                 'Candidat 4': 33}))