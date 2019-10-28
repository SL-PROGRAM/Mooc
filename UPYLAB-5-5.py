"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé



Écrire une fonction trans(text, replaceA, replaceB) qui reçoit trois paramètres :

    text : une chaîne de caractères

    replaceA : un couple de la forme (oldA, newA) où oldA est un caractère et newA une chaîne de caractères

    replaceB : un couple de la forme (oldB, newB) où oldB est un caractère et newB une chaîne de caractères

et qui renvoie le résultat de la transformation suivante :

chaque occurrence du symbole oldA dans la chaîne text est remplacée par la chaîne newA, et simultanément,
chaque occurrence du symbole oldB est remplacée par la chaîne newB.


"""

def trans(text, replaceA, replaceB):
    text = list(text)
    oldA, newA = replaceA
    oldB, newB = replaceB

    for i in range(len(text)):
        if text[i] == oldA:
            text[i] = newA

        elif text[i] == oldB:
            text[i] = newB
    text = ''.join(text)
    return text


print(trans('police', ('p', 'PP'), ('i', 'ii')))

