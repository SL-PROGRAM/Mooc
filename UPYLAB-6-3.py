"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Lors de prises de notes, il nous arrive souvent de remplacer des mots par des abréviations (bonjour est remplacé par
bjr par exemple).

Nous allons utiliser un dictionnaire qui associe à chacune de ces abréviations sa signification.

Écrire une fonction substitue(message, abreviation) qui renvoie une copie de la chaîne de caractères message dans
laquelle les mots qui figurent parmi les clés du dictionnaire abreviation sont remplacés par leur signification (valeur).


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction substitue. Le code que vous soumettez à
     UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
     input ou à print.

    Pour simplifier, on suppose que les mots de la chaîne message sont séparés par des espaces.

    Vous pourrez supposer que les arguments passés à la fonction sont du bon type.



"""

def substitue(message, abreviation):
    words = message.split(" ")
    lst_message = []
    for word in words:
        if word in abreviation:
            lst_message += [ abreviation[word]]
        else:
            lst_message += [word]
    message = " ".join(lst_message)
    return message

print(substitue('C. N. cpt 2 to inf', {'cpt': 'counted', '2': '2 times', 'inf': 'infinity', 'C.': 'Chuck', 'N.': 'Norris'}))