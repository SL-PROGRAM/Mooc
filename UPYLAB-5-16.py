"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Énoncé

(D’après une idée de Jacky Trinh - 11/02/2018)

Joao vient d’arriver dans notre pays depuis le Portugal. Il a encore du mal avec la langue française.
Malgré ses efforts considérables, il fait une faute d’orthographe quasi à chaque mot. Son souci est qu’il n’arrive pas
toujours à écrire un mot correctement sans se tromper à une lettre près. Ainsi pour écrire « bonjour », il peut écrire
« binjour ». Pour remédier à ce problème, Joao utilise un correcteur orthographique. Malheureusement, Joao a un examen
aujourd’hui et il a oublié son petit correcteur.

Afin de l’aider, nous vous demandons d’écrire une fonction correcteur(mot, liste_mots) où mot est le mot que Joao
 écrit et liste_mots est une liste qui contient les mots (ayant la bonne orthographe) que Joao est susceptible
  d’utiliser.

Cette fonction doit retourner le mot dont l’orthographe a été corrigée.


Consignes

    Pour cet exercice, vous pourrez utiliser la fonction distance_mots(mot_1, mot_2) que vous avez précédemment codée
    et qui donne la distance entre deux mots de même longueur. N’oubliez pas alors de mettre aussi le code de
    cette fonction dans votre solution.

    Le correcteur orthographique demandé est une version simple ; les mots en paramètre auront au maximum une seule
    lettre qui diffère par rapport à la bonne orthographe.

    Nous ne prenons pas en compte les mots avec accents, ni les mots composés de tiret, d’apostrophes, d’espace,..

    liste_mots ne contient pas de mots qui se ressemblent ; si Joao écrit le mot « liee », il se peut en effet que cela
    représente le mot « lire » ou « lier ». Afin d’éviter cette confusion, deux mots de même longueur de la liste sont
    au moins à une distance de 3. Il n’y aura ainsi qu’un seul mot dans liste_mots répondant au problème.

    Vous pouvez supposer que Joao soit arrive à écrire des mots sans fautes, soit fait au plus une erreur.




"""


def correcteur(mot, liste_mots):
    mot_cor = None
    for mot_bon in liste_mots:
        if len(mot) == len(mot_bon):
            dist = distance_mots(mot, mot_bon)
            if dist <= 1:
                mot_cor = mot_bon
                break
    return mot_cor

def distance_mots(mot_1, mot_2):
    dist = len(mot_1)
    for i in range(len(mot_1)):
        if mot_1[i] == mot_2[i]:
            dist -= 1

    return dist


