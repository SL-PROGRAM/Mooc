"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé




Écrire une fonction longueur(*points) qui reçoit en paramètres un nombre arbitraire de points (tuples de deux
composantes), et retourne la longueur de la ligne brisée correspondante.

Cette longueur se calcule en additionnant les longueurs des segments formés par deux points consécutifs.


"""

def longueur(*points):
    def distance_points(point1, point2):
        import math
        x1, y1 = point1
        x2, y2 = point2

        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


    i = 1
    long = 0
    while (len(points)> i):
        long += distance_points(points[i-1], points[i])
        i+=1
    return long



print(longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0)))