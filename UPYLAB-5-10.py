"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Enoncé

Écrire une fonction prime_numbers qui reçoit comme paramètre un nombre entier nb et qui renvoie la liste des nb
premiers nombres premiers.

Si le paramètre n’est pas du type attendu, ou ne correspond pas à un nombre entier positif ou nul, la fonction
renvoie None.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction prime_numbers. Le code que vous soumettez
    à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.

    On rappelle qu’un nombre premier est un entier naturel qui possède exactement deux diviseurs distincts et
    positifs, 1 et lui-même.



"""

def prime_numbers(nb):
    if type(nb) != int or nb<0:
        list = None
    else:
        k = 2
        list = []
        while len(list) < nb:
            test = True
            for j in range(2,k-1):
                print(j)
                if k % j == 0:
                    test = False
                    break
            if test == True:
                list.append(k)
            k+=1
    return list


print(prime_numbers(15))


