"""Auteur: Simon LEYRAL
   Date : novembre 2017


Écrire une fonction compteur_lettres(texte) qui renvoie un dictionnaire contenant toutes les lettres de l’alphabet
associées à leur nombre d’apparition dans texte.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction compteur_lettres. Le code que vous soumettez
    à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.

    Les clés du dictionnaire seront les lettres de l’alphabet en minuscule. Si le texte contient des majuscules,
    celles-ci seront comptabilisées comme la lettre minuscule correspondante.

    Le texte passé en paramètre ne comportera aucun caractère accentué.

    Les espaces et autres caractères de ponctuation doivent être ignorés.



"""
def compteur_lettres(texte):
    texte = texte.lower()
    letters = dict([(l, 0) for l in "abcdefghijklmnopqrstuvwxyz"])
    for letter in texte:
        if letter not in letters:
            continue
        letters[letter] += 1
    return letters

