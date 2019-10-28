""" Auteur: Simon LEYRAL
    date : Octobre 2019
    But du programme :
    Le programme suivant calcule la circonférence
    et l’aire d’un disque dont le rayon est donné
    en input
    Entrée: rayon : le rayon du disque
    Sorties: la circonférence du disque
             l'aire du disque
"""
#importation de la fonction pi du module math
from math import pi


rayon = float(input("Veuillez donner le rayon : "))  # lecture du rayon de mon disque
circ = 2 * pi  * rayon                    # calcul de la circonférence
aire = pi * rayon **  2                   # calcul de l'aire
# Affichage des résultats
print("Circonférence : ", circ)
print("Aire          : ", aire)