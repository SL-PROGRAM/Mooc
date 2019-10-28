"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé



Écrire un programme qui teste si pour une configuration donnée, l’écureuil va ou non atteindre un moment la noisette.
Il reçoit deux valeurs entières en entrée, une valeur saut et une valeur position_cible toutes deux entre 1 et 99.

Le programme va calculer une valeur position_courante, initialement la valeur 0, et vérifier si en calculant de
façon répétitive la valeur position_courante, celle-ci aboutira un moment à la valeur position_cible.

Notez que pour calculer la valeur suivante de position_courante (initialement mise à 0), il faut incrémenter
la valeur actuelle de position_courante de la valeur saut et ensuite, si le résultat est plus grand ou égal à 100,
calculer la position en faisant un modulo 100 de la valeur obtenue (ce qui donne à chaque fois une valeur position_
courante entre 0 et 99). (Notez que l’on peut systématiquement faire le modulo 100 du résultat sans tester si position_
courante est ou non supérieur à 100 pour obtenir sa bonne valeur).

Notez également, pour ne pas épuiser mon écureuil sans fin, que s’il atteint à nouveau la barreau 0, j’arrête
l’expérience sachant qu’il prendra toujours les mêmes barreaux sans jamais atteindre position_cible (la noisette).

A la fin votre programme dira si oui ou non la noisette a été atteinte ou non.

En pratique, après avoir lu les deux valeurs saut et position_cible, votre programme affichera chaque valeur de
position_courante sur une ligne différente à partir de la seconde valeur (pas la position_courante initiale qui
vaut toujours 0). La dernière position_courante affichée sera soit 0 soit la dernière valeur de position_courante
avant qu’elle n’aie la valeur de position_cible, si l’écureuil trouve la noisette. Votre programme terminera en
affichant, sur une nouvelle ligne, le message donnant le résultat :

    "Cible atteinte" si l’écureuil a trouvé la noisette,

    "Pas trouvé" si l’écureuil est revenu en position 0 sans trouver la noisette.

Vous pouvez supposer que les valeurs lues sont bien des entiers qui respectent les consignes.




"""

saut = int(input())
position_cible = int(input())

position_courante = 0
turn = 0

while (position_courante != 0 or turn == 0) and position_courante != position_cible:
    position_courante += saut
    position_courante = position_courante%100
    turn = 1

    if position_courante == position_cible:
        print("Cible atteinte")
    elif position_courante == 0:
        print(position_courante)
        print("Pas trouvé")
    else:
        print(position_courante)


