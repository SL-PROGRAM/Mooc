"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Énoncé

Problème

Écrivez un script qui n’affiche que les mots qui ne contiennent pas de “e” et calculez le pourcentage de ceux-ci par
 rapport à l’ensemble des mots du fichier mots.txt.

"""

count = 0
count_without = 0
for mot in open("mots.txt", encoding="utf-8"):
    count += 1
    if "e" not in mot:
        count_without += 1
        print(mot.strip())

print(count_without/count*100)