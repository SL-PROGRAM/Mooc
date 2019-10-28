"""Auteur: Simon LEYRAL
   Date : Octobre 2017
   But du programme : calcule les ingrédients nécessaires
   pour préparer de la mousse au chocolat pour n personnes
   Entrée: n (nombre de personnes)
   Sorties: nombre d'oeufs,
            quantité en gramme de chocolat,
            nombre de sachets de sucre vanillé
"""
n = int(input("nombre de personnes : "))     # entrée: nombre de personnes
# calcule et affiche les résultats
print("nombre d'oeufs : ", round(3 * n / 4))
print("quantité de chocolat en grammes : ", round(100 * n / 4))
print("quantité de sucre_vanillé : ", max(round(n / 4), 1))
