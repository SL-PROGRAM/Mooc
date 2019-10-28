"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Écrire une fonction my_pow qui prend comme paramètres un nombre entier m et un nombre flottant b, et qui renvoie une
liste contenant les m premières puissances de b, c’est-à-dire une liste contenant les nombres allant de b^0 à b^{m - 1}.

Si le type des paramètres n’est pas celui attendu, la fonction retournera la valeur None.


Consignes

Dans cet exercice, il vous est demandé d’écrire seulement la fonction my_pow.

Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait
en particulier aucun appel à input ou à print.


"""

def anagrammes(v, w):
    if len(v) != len(w):
        test = False
    else:
        for i in v:
            if i not in w:
                test = False
                break
            else:
                test = True
        for i in w:
            if i not in v:
                test = False
                break
            else:
                test = True
    return test

print(anagrammes("aaaa", "vase"))