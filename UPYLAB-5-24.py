"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Enoncé



Écrire une fonction print_mat(M) qui reçoit une matrice M en paramètre et affiche son contenu.

Les éléments d’une même ligne de la matrice seront affichés sur une même ligne, et séparés par une espace, les éléments
de la ligne suivante étant affichés sur une nouvelle ligne.


Consignes

    Important : Afin de permettre à UpyLaB de tester votre fonction, votre code contiendra également, après le code
    de la définition de la fonction print_mat, les instructions suivantes :

ma_matrice = eval(input())
print_mat(ma_matrice)

    Si la matrice vide [] est passée en argument , la fonction affiche une ligne vide.

    Dans cet exercice, la présence d’espaces en fin de ligne ne sera pas sanctionnée. Par contre, veillez à ce qu’il
     n’y ait pas de ligne supplémentaire.


"""


def print_mat(M):
    for lst in M:
        lign = ""
        for elem in lst:
            lign += str(elem)+" "
        print(lign)

print_mat([[1,2,30],[1,2,4]])