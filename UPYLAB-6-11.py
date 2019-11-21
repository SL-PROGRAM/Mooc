"""Auteur: Simon LEYRAL
   Date : novembre 2017



    Écrire une fonction file_histogram(fileName) qui prend en paramètre le nom, sous forme d’une chaîne de caractères,
    d’un fichier texte, et qui renvoie un dictionnaire associant à chaque caractère du texte contenu dans ce fichier
    son nombre d’occurrences.

    Écrire une fonction vowels_histogram(fileName) qui prend en paramètre le nom, sous forme d’une chaîne de caractères,
     d’un fichier texte, et qui renvoie un dictionnaire contenant le nombre d’occurrences de chaque suite de voyelles
     non accentuées présentes dans le texte contenu dans le fichier.

    Écrire une fonction words_by_length(fileName) qui prend en paramètre le nom, sous forme d’une chaîne de caractères,
    d’un fichier texte, et qui renvoie un dictionnaire associant à une longueur l la liste triée (dans l’ordre utf-8
    croissant) des mots de longueur l présents dans le texte contenu dans le fichier. Ces mots seront écrits en
    minuscules.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement des fonctions. Le code que vous soumettez à UpyLaB doit
    donc comporter uniquement la définition de ces fonctions, et ne fait en particulier aucun appel à input ou à print.

    Les fichiers utilisés par UpyLaB pour tester votre code sont :

            https://upylab.ulb.ac.be/pub/data/words.txt

            https://upylab.ulb.ac.be/pub/data/le-petit-prince.txt

            https://upylab.ulb.ac.be/pub/data/Zola.txt

    Pour la fonction vowels_histogram, notez que si l’on trouve « ou » par exemple, il ne faut pas comptabiliser une
    occurrence de « o » ni de « u ».

Par ailleurs, la casse devra être respectée : la même suite de voyelles en minuscule et en majuscule donnera lieu à
deux clés différentes du dictionnaire.

    Pour la fonction words_by_length, on supposera qu’un mot est une séquence de caractères alphabétiques. La méthode
    isalpha() pourra être utile.

Par exemple, la chaîne de caractères 'cat4dog' sera considérée comme formant deux mots : 'cat' et 'dog'.

Veillez aussi à ce qu’un même mot n’apparaisse pas plusieurs fois dans la même liste.


"""


def file_histogram(fileName):
    histogram = {}
    with open(fileName) as textes:
        for texte in textes:
            for letter in texte:
                if letter in histogram:
                    histogram[letter] += 1
                else:
                    histogram[letter] = 1
    return histogram


def vowels_histogram(fileName):
    histogram = {}
    with open(fileName) as textes:
        v = ""
        for texte in textes:
            for letter in texte:
                vowels = "aeiouyAEIOUY"
                if letter in vowels:
                    v += letter
                elif v != "":
                    if v in histogram:
                        histogram[v] += 1
                    else:
                        histogram[v] = 1
                    v = ""
    return histogram


def words_by_length(fileName):
    histogram = {}
    with open(fileName) as textes:
        w = ""
        for texte in textes:
            for letter in texte:
                letter = letter.lower()
                if letter.isalpha():
                    w += letter
                elif w != "":
                    if len(w) in histogram:
                        if w not in histogram[len(w)]:
                            histogram[len(w)] += [w]
                    else:
                        histogram[len(w)] = [w]
                    w = ""
    for elem in histogram:
        histogram[elem] = sorted(histogram[elem])
    return histogram


print(file_histogram("Zola.txt"))
print(vowels_histogram("Zola.txt"))
print(words_by_length("Zola.txt"))

