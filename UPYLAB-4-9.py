"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Pierre-feuille-ciseaux (voir Pierre-papier-ciseaux sur Wikipedia) est un jeu effectué avec les mains et opposant un
ou plusieurs joueurs. Ici nous nous supposerons qu’il y a deux joueurs : l’ordinateur et le joueur lui-même.

Déroulement du jeu

Les deux joueurs choisissent simultanément un des trois coups possibles en le symbolisant de la main :

    Poing fermé : Pierre ;

    Main ouverte, doigts collés les uns aux autres : Feuille ;

    Main avec pouce, annulaire et auriculaire fermé, index et majeur ouvert en forme de V : Ciseaux.

Résultat du jeu :

    La pierre bat les ciseaux (en les émoussant),

    les ciseaux battent la feuille (en la coupant),

    la feuille bat la pierre (en l’enveloppant).

Ainsi chaque coup bat un autre coup, fait match nul contre le deuxième (son homologue) et est battu par le troisième.

Écrire une fonction bat(joueur_1, joueur_2) où joueur_1 et joueur_2 ont chacun une valeur entière 0, 1 ou 2,
qui encode ce que le joueur a fait comme coup (0 : PIERRE, 1 : FEUILLE, 2 : CISEAUX) qui renvoie un résultat booléen :

    vrai si joueur_1 bat le joueur_2 :

    faux si joueur_2 bat joueur_1 ou fait match nul contre lui.



Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction bat. Le code que vous soumettez à UpyLaB doit
    donc comporter uniquement la définition de cette fonction, éventuellement accompagné des trois définitions des
    constantes PIERRE, FEUILLE, CISEAUX , et ne fait en particulier aucun appel à inputou à print.

    Il n’est pas demandé que la fonction bat teste le type ou les valeurs des paramètres reçus.



"""

def bat(joueur_1, joueur_2 ):
    PIERRE = 0
    FEUILLE = 1
    CISEAUX = 2


    if joueur_1 == PIERRE and joueur_2 != CISEAUX:
        bat = False
    elif joueur_1 == FEUILLE and joueur_2 != PIERRE:
        bat = False
    elif joueur_1 == CISEAUX and joueur_2 != FEUILLE:
        bat = False
    else:
        bat = True

    return bat

