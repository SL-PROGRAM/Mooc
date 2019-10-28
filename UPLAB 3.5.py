"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Écrire un programme qui lit en entrée deux nombres entiers strictement positifs,
et qui vérifie qu’aucun des deux n’est un diviseur de l’autre.

Si tel est bien le cas, le programme imprime True. Sinon, il imprime False.


"""
joueur =int(input())
tirage =int(input())
mise = 10

if joueur == tirage and tirage >=0 and tirage <= 16:
    if joueur <= 12 and joueur >= 0:
        print(mise*12)
elif joueur:
        print(2*mise)
else:
    print("0")
