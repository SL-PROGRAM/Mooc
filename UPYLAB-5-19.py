"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Énoncé



Écrire un programme dont le but est d’écrire l’histoire dont vous êtes le héros (ou qui que vous vouliez).

Le programme va :

    d’abord lire une chaîne de caractères précisant le nom du fichier à traiter contenant le canevas de l’histoire ;

    ensuite la liste des noms de personnages de l’histoire, sous forme d’une chaîne de caractères, chaque personnage
    sur une ligne ; cette liste est terminée par la chaîne de caractère "FINI" qui signifie que la liste est complète.

Le texte du fichier nom contient une histoire où les noms des personnages sont remplacés par des numéros, à partir de
zéro, entre accolades, par exemple : {0}, {1} …

Votre programme doit ouvrir le fichier nom, en lire le texte, et remplacer chaque {i} où i est un numéro par le nom du
personnage correspondant ({0} étant le premier personnage de la liste lue, {1} le second, etc).

Le texte ainsi modifié sera imprimé sans changer autre chose au texte.

Consignes

    Vous pouvez supposer que le fichier existe bien et est en format UTF-8.

    Les fichiers utilisés par UpyLaB pour tester la fonction sont accessibles aux adresses suivantes :

            https://upylab.ulb.ac.be/pub/data/histoire_1.txt

            https://upylab.ulb.ac.be/pub/data/histoire_2.txt


"""

nom = str(input())  # nom du fichier
personnage = str(input())  # nom des personnages
personnages = []
while personnage != "FINI":
    personnages.append(personnage)
    personnage = str(input())

f_nom = open(nom, encoding="utf-8")  # ouverture du fichier

for lign in f_nom:
    histoire = lign.strip()
    h = histoire.split()

    for i in range(len(personnages)):
        for elem in range(len(h)):
            if "{" + str(i) + "}" in h[elem]:
                h[elem] =h[elem].replace("{" + str(i) + "}", personnages[i])
    h = " ".join(h)
    print(h)
f_nom.close()
