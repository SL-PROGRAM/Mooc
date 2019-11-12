"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Écrire une fonction belongs_to_file(word, filename) qui reçoit deux chaînes de caractères en paramètre. La première
correspond à un mot, et la deuxième au nom d’un fichier contenant une liste de mots, chacun sur sa propre ligne. La
fonction vérifie si le mot figure dans cette liste, et retourne True si c’est bien le cas, False sinon.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction belongs_to_file. Le code que vous soumettez
    à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.

    Vous pourrez supposer que le fichier passé en paramètre contient bien une liste de mots, chacun sur sa propre ligne.

    N’oubliez pas d’ouvrir le fichier dans le code de la fonction.

    Le fichier utilisé par UpyLaB pour effectuer les tests est disponible à l’adresse :
        https://upylab.ulb.ac.be/pub/data/words.txt



"""
def belongs_to_file(word, filename):
    test = False
    with open(filename, encoding="UTF-8") as words:
       for w in words:
            w = w.strip()
            if w == word:
               test = True
               break
    return test



print(belongs_to_file("zwitter", "words.txt"))

